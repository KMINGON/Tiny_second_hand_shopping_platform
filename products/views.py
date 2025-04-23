from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, ProductImage
from .forms import ProductForm, ProductImageForm
from django.http import HttpResponseForbidden
from django.views.decorators.http import require_POST
from django.db.models import Q

def product_list_view(request):
    query = request.GET.get('q', '')
    products = Product.objects.all()

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    products = products.order_by('-created_at')
    return render(request, 'products/product_list.html', {
        'products': products,
        'query': query
    })

@login_required
def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        image_form = ProductImageForm(request.POST, request.FILES)

        if form.is_valid() and image_form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()

            image = image_form.cleaned_data['image']
            ProductImage.objects.create(product=product, image=image)

            return redirect('/')  # 또는 상품 목록으로 이동
    else:
        form = ProductForm()
        image_form = ProductImageForm()
    return render(request, 'products/product_create.html', {
        'form': form,
        'image_form': image_form,
    })

def product_detail_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_detail.html', {'product': product})

@login_required
def product_edit_view(request, id):
    product = get_object_or_404(Product, id=id)

    # 권한 확인: 작성자만 수정 가능
    if product.user != request.user:
        return HttpResponseForbidden("접근 권한이 없습니다.")

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        image_form = ProductImageForm(request.POST, request.FILES)

        if form.is_valid() and image_form.is_valid():
            form.save()

            # 새 이미지가 업로드되면 기존 것 삭제하고 대체
            if image_form.cleaned_data.get('image'):
                product.productimage_set.all().delete()
                ProductImage.objects.create(product=product, image=image_form.cleaned_data['image'])

            return redirect('product_detail', id=product.id)
    else:
        form = ProductForm(instance=product)
        image_form = ProductImageForm()
    return render(request, 'products/product_edit.html', {
        'form': form,
        'image_form': image_form,
        'product': product
    })

@login_required
@require_POST
def product_delete_view(request, id):
    product = get_object_or_404(Product, id=id)

    if product.user != request.user:
        return HttpResponseForbidden("접근 권한이 없습니다.")

    # 이미지 삭제
    for img in product.productimage_set.all():
        img.image.delete(save=False)
        img.delete()

    # 상품 삭제
    product.delete()
    return redirect('product_list')