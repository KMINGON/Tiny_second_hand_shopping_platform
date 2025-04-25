from django.contrib import admin
from .models import Chat, ChatReport
from django.utils.html import format_html

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'message', 'created_at', 'is_hidden', 'display_hidden_status')
    list_filter = ('created_at', 'is_hidden')
    search_fields = ('message', 'sender__username', 'receiver__username')
    actions = ['hide_messages', 'unhide_messages']
    
    def display_hidden_status(self, obj):
        if obj.is_hidden:
            return format_html('<span style="color: red;">숨김</span>')
        return format_html('<span style="color: green;">표시</span>')
    display_hidden_status.short_description = '상태'
    
    def hide_messages(self, request, queryset):
        queryset.update(is_hidden=True)
    hide_messages.short_description = "선택된 메시지를 숨김"
    
    def unhide_messages(self, request, queryset):
        queryset.update(is_hidden=False)
    unhide_messages.short_description = "선택된 메시지를 표시"

@admin.register(ChatReport)
class ChatReportAdmin(admin.ModelAdmin):
    list_display = ('reporter', 'message', 'reason', 'reported_at', 'quick_actions')
    list_filter = ('reported_at',)
    search_fields = ('reason', 'reporter__username', 'message__message')
    actions = ['hide_reported_messages']
    
    def quick_actions(self, obj):
        return format_html(
            '<a href="/admin/chat/chat/{}/change/">메시지 관리</a>',
            obj.message.id
        )
    quick_actions.short_description = '빠른 액션'
    
    def hide_reported_messages(self, request, queryset):
        for report in queryset:
            report.message.is_hidden = True
            report.message.save()
    hide_reported_messages.short_description = "신고된 메시지 숨김"
