from django.contrib import admin
from .models import UserReport, ChatReport

@admin.register(UserReport)
class UserReportAdmin(admin.ModelAdmin):
    list_display = ('reporter', 'reported_user', 'reason', 'reported_at')
    list_filter = ('reported_at',)
    search_fields = ('reason', 'reporter__username', 'reported_user__username')

@admin.register(ChatReport)
class ChatReportAdmin(admin.ModelAdmin):
    list_display = ('reporter', 'message', 'reason', 'reported_at')
    list_filter = ('reported_at',)
    search_fields = ('reason', 'reporter__username', 'message__message')
