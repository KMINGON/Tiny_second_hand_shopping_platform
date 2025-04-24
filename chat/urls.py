# chat/urls.py
from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('user/<int:user_id>/', views.private_chat_view, name='private_chat'),  # /chat/user/3/
    path('chat_list/', views.chat_list_view, name='chat_list'),  # /chat/chat_list/
    path('global_chat/', views.global_chat_view, name='global_chat'),  # /chat/global_chat/
    path('report/<int:message_id>/', views.report_chat_view, name='report_chat'),  # /chat/report/1/
    path('my_reports/', views.my_reports_view, name='my_reports'),  # /chat/my_reports/
]
