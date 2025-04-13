# products/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list_view, name='product_list'),         # /products/
    path('new/', views.product_create_view, name='product_create'), # /products/new/
    path('<int:id>/', views.product_detail_view, name='product_detail'), # /products/5/
]
