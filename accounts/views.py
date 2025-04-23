from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.decorators import login_required

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

def logout_view(request):
    return render(request, 'accounts/logout.html')

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
