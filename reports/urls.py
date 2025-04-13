# reports/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_create_view, name='report_create'),  # /reports/
]
