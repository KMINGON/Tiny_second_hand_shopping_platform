from django.contrib import admin
from .models import Product, ProductImage
from django.utils.html import format_html

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'user', 'created_at', 'is_hidden', 'display_hidden_status')
    list_filter = ('created_at', 'is_hidden')
    search_fields = ('name', 'description', 'user__username')
    inlines = [ProductImageInline]
    actions = ['hide_products', 'unhide_products']
    
    def display_hidden_status(self, obj):
        if obj.is_hidden:
            return format_html('<span style="color: red;">숨김</span>')
        return format_html('<span style="color: green;">표시</span>')
    display_hidden_status.short_description = '상태'
    
    def hide_products(self, request, queryset):
        queryset.update(is_hidden=True)
    hide_products.short_description = "선택된 상품을 숨김"
    
    def unhide_products(self, request, queryset):
        queryset.update(is_hidden=False)
    unhide_products.short_description = "선택된 상품을 표시"

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
    search_fields = ('product__name',)
