from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.html import format_html
from django.db.models import Count, Q
from products.models import Product
from chat.models import Chat
from reports.models import UserReport, ChatReport

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_admin', 'display_status', 
                   'product_count', 'chat_count', 'report_count', 'reported_count')
    list_filter = ('is_active', 'is_admin', 'date_joined')
    search_fields = ('username', 'email', 'bio')
    actions = ['activate_users', 'deactivate_users', 'make_admin', 'remove_admin']
    
    def display_status(self, obj):
        if obj.is_active:
            return format_html('<span style="color: green;">활성</span>')
        return format_html('<span style="color: red;">비활성</span>')
    display_status.short_description = '상태'
    
    def product_count(self, obj):
        count = Product.objects.filter(user=obj).count()
        return format_html(f'<a href="/admin/products/product/?user__id__exact={obj.id}">{count}</a>')
    product_count.short_description = '상품 수'
    
    def chat_count(self, obj):
        count = Chat.objects.filter(Q(sender=obj) | Q(receiver=obj)).count()
        return format_html(f'<a href="/admin/chat/chat/?sender__id__exact={obj.id}">{count}</a>')
    chat_count.short_description = '채팅 수'
    
    def report_count(self, obj):
        user_reports = UserReport.objects.filter(reporter=obj).count()
        chat_reports = ChatReport.objects.filter(reporter=obj).count()
        return format_html(f'<a href="/admin/reports/userreport/?reporter__id__exact={obj.id}">{user_reports + chat_reports}</a>')
    report_count.short_description = '신고 수'
    
    def reported_count(self, obj):
        user_reports = UserReport.objects.filter(reported_user=obj).count()
        return format_html(f'<a href="/admin/reports/userreport/?reported_user__id__exact={obj.id}">{user_reports}</a>')
    reported_count.short_description = '신고당한 수'
    
    def activate_users(self, request, queryset):
        queryset.update(is_active=True)
    activate_users.short_description = "선택된 사용자 활성화"
    
    def deactivate_users(self, request, queryset):
        queryset.update(is_active=False)
    deactivate_users.short_description = "선택된 사용자 비활성화"
    
    def make_admin(self, request, queryset):
        queryset.update(is_admin=True)
    make_admin.short_description = "선택된 사용자를 관리자로 지정"
    
    def remove_admin(self, request, queryset):
        queryset.update(is_admin=False)
    remove_admin.short_description = "선택된 사용자의 관리자 권한 제거"