# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:user_id>/', views.private_chat_view, name='private_chat'),  # /chat/user/3/
    path('chat_list/', views.chat_list_view, name='chat_list'),  # /chat/chat_list/
    path('global_chat/', views.global_chat_view, name='global_chat'),  # /chat/global_chat/
]
