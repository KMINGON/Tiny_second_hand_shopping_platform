from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('chat/<int:message_id>/', views.report_chat_view, name='report_chat'),
    path('my_reports/', views.my_reports_view, name='my_reports'),
    path('accounts/report/<int:user_id>/', views.report_user_view, name='report_user'),
]