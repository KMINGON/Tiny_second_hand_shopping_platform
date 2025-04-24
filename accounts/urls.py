# accounts/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('mypage/', views.mypage_view, name='mypage'),
    path('password/', PasswordChangeView.as_view(
        template_name='accounts/password_change.html',
        success_url='/accounts/mypage/'
    ), name='password_change'),
    path('profile/<int:user_id>/', views.user_profile, name='user_profile'),
]