from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from products.models import Product
from chat.models import Chat
from django.db.models import Q
from django.contrib.auth.views import LogoutView

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    return render(request, 'accounts/login.html')

class CustomLogoutView(LogoutView):
    next_page = '/'

@login_required
def mypage_view(request):
    user = request.user
    if request.method == 'POST':
        bio = request.POST.get('bio')
        account_number = request.POST.get('account_number')
        user.bio = bio
        user.account_number = account_number
        user.save()
        return redirect('mypage')
    return render(request, 'accounts/mypage.html', {'user': user})

@login_required
def user_profile(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)
    user_products = Product.objects.filter(user=target_user).order_by('-created_at')
    
    context = {
        'target_user': target_user,
        'user_products': user_products,
    }
    return render(request, 'accounts/user_profile.html', context)
