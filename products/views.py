from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, ProductImage
from .forms import ProductForm, ProductImageForm

def product_list_view(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'products/product_list.html', {'products': products})

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
