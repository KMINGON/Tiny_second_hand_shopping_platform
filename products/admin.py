from django.contrib import admin
from .models import Product, ProductImage
from django.utils.html import format_html
from django.db.models import Count, Q
from django.contrib import messages

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'user', 'created_at', 'is_hidden', 'display_hidden_status', 
                   'image_count', 'user_status', 'quick_actions')
    list_filter = ('created_at', 'is_hidden')
    search_fields = ('name', 'description', 'user__username')
    inlines = [ProductImageInline]
    actions = ['hide_products', 'unhide_products', 'delete_products']
    
    def display_hidden_status(self, obj):
        if obj.is_hidden:
            return format_html('<span style="color: red;">숨김</span>')
        return format_html('<span style="color: green;">표시</span>')
    display_hidden_status.short_description = '상태'
    
    def image_count(self, obj):
        count = obj.productimage_set.count()
        return format_html(f'<a href="/admin/products/productimage/?product__id__exact={obj.id}">{count}</a>')
    image_count.short_description = '이미지 수'
    
    def user_status(self, obj):
        if obj.user.is_active:
            return format_html('<span style="color: green;">활성</span>')
        return format_html('<span style="color: red;">비활성</span>')
    user_status.short_description = '사용자 상태'
    
    def quick_actions(self, obj):
        return format_html(
            '<a href="/admin/accounts/customuser/{}/change/">사용자 관리</a> | '
            '<a href="/admin/chat/chat/?sender__id__exact={}">채팅 관리</a>',
            obj.user.id, obj.user.id
        )
    quick_actions.short_description = '빠른 액션'
    
    def hide_products(self, request, queryset):
        queryset.update(is_hidden=True)
        messages.success(request, f'{queryset.count()}개의 상품이 숨김 처리되었습니다.')
    hide_products.short_description = "선택된 상품을 숨김"
    
    def unhide_products(self, request, queryset):
        queryset.update(is_hidden=False)
        messages.success(request, f'{queryset.count()}개의 상품이 표시되었습니다.')
    unhide_products.short_description = "선택된 상품을 표시"
    
    def delete_products(self, request, queryset):
        count = queryset.count()
        for product in queryset:
            # 이미지 삭제
            for img in product.productimage_set.all():
                img.image.delete(save=False)
                img.delete()
            # 상품 삭제
            product.delete()
        messages.success(request, f'{count}개의 상품이 삭제되었습니다.')
    delete_products.short_description = "선택된 상품 삭제"

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image_preview', 'product_status')
    search_fields = ('product__name',)
    
    def image_preview(self, obj):
        return format_html(f'<img src="{obj.image.url}" style="max-height: 100px;" />')
    image_preview.short_description = '이미지 미리보기'
    
    def product_status(self, obj):
        if obj.product.is_hidden:
            return format_html('<span style="color: red;">숨김</span>')
        return format_html('<span style="color: green;">표시</span>')
    product_status.short_description = '상품 상태'
