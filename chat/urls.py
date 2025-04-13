# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('global/', views.global_chat_view, name='global_chat'),       # /chat/global/
    path('user/<int:user_id>/', views.private_chat_view, name='private_chat'),  # /chat/user/3/
]
