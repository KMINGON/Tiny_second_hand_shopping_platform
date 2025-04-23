# products/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list_view, name='product_list'),         # /products/
    path('new/', views.product_create_view, name='product_create'), # /products/new/
    path('<int:id>/', views.product_detail_view, name='product_detail'), # /products/5/
    path('<int:id>/edit/', views.product_edit_view, name='product_edit'), # /products/5/edit/
    path('<int:id>/delete/', views.product_delete_view, name='product_delete'), # /products/5/delete/
]
