from django.contrib import admin
from .models import UserReport, ChatReport
from django.utils.html import format_html
from django.db.models import Count
from django.contrib import messages

@admin.register(UserReport)
class UserReportAdmin(admin.ModelAdmin):
    list_display = ('reporter', 'reported_user', 'reason', 'reported_at', 'status', 'quick_actions')
    list_filter = ('reported_at',)
    search_fields = ('reason', 'reporter__username', 'reported_user__username')
    actions = ['auto_process_reports', 'mark_as_processed']
    
    def status(self, obj):
        if obj.reported_user.is_active:
            return format_html('<span style="color: green;">활성</span>')
        return format_html('<span style="color: red;">비활성</span>')
    status.short_description = '사용자 상태'
    
    def quick_actions(self, obj):
        return format_html(
            '<a href="/admin/accounts/customuser/{}/change/">사용자 관리</a> | '
            '<a href="/admin/products/product/?user__id__exact={}">상품 관리</a> | '
            '<a href="/admin/chat/chat/?sender__id__exact={}">채팅 관리</a>',
            obj.reported_user.id, obj.reported_user.id, obj.reported_user.id
        )
    quick_actions.short_description = '빠른 액션'
    
    def auto_process_reports(self, request, queryset):
        for report in queryset:
            # 3회 이상 신고당한 사용자는 자동 비활성화
            report_count = UserReport.objects.filter(reported_user=report.reported_user).count()
            if report_count >= 3:
                report.reported_user.is_active = False
                report.reported_user.save()
                messages.success(request, f'{report.reported_user.username} 사용자가 자동 비활성화되었습니다.')
    auto_process_reports.short_description = "자동 처리 (3회 이상 신고시 비활성화)"
    
    def mark_as_processed(self, request, queryset):
        messages.success(request, f'{queryset.count()}개의 신고가 처리되었습니다.')
    mark_as_processed.short_description = "선택된 신고를 처리 완료로 표시"

@admin.register(ChatReport)
class ChatReportAdmin(admin.ModelAdmin):
    list_display = ('reporter', 'message', 'reason', 'reported_at', 'status', 'quick_actions')
    list_filter = ('reported_at',)
    search_fields = ('reason', 'reporter__username', 'message__message')
    actions = ['auto_hide_messages', 'mark_as_processed']
    
    def status(self, obj):
        if obj.message.is_hidden:
            return format_html('<span style="color: red;">숨김</span>')
        return format_html('<span style="color: green;">표시</span>')
    status.short_description = '메시지 상태'
    
    def quick_actions(self, obj):
        return format_html(
            '<a href="/admin/chat/chat/{}/change/">메시지 관리</a> | '
            '<a href="/admin/accounts/customuser/{}/change/">사용자 관리</a>',
            obj.message.id, obj.message.sender.id
        )
    quick_actions.short_description = '빠른 액션'
    
    def auto_hide_messages(self, request, queryset):
        for report in queryset:
            # 2회 이상 신고당한 메시지는 자동 숨김
            report_count = ChatReport.objects.filter(message=report.message).count()
            if report_count >= 2:
                report.message.is_hidden = True
                report.message.save()
                messages.success(request, f'메시지가 자동 숨김 처리되었습니다.')
    auto_hide_messages.short_description = "자동 처리 (2회 이상 신고시 숨김)"
    
    def mark_as_processed(self, request, queryset):
        messages.success(request, f'{queryset.count()}개의 신고가 처리되었습니다.')
    mark_as_processed.short_description = "선택된 신고를 처리 완료로 표시"
