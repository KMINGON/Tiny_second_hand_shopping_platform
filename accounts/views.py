from django.shortcuts import render

def signup_view(request):
    return render(request, 'accounts/signup.html')

def login_view(request):
    return render(request, 'accounts/login.html')

def logout_view(request):
    return render(request, 'accounts/logout.html')

def mypage_view(request):
    return render(request, 'accounts/mypage.html')
