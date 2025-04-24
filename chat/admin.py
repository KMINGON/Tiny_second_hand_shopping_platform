from django.contrib import admin
from .models import Chat, ChatReport

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('message', 'sender__username', 'receiver__username')

@admin.register(ChatReport)
class ChatReportAdmin(admin.ModelAdmin):
    list_display = ('reporter', 'message', 'reason', 'reported_at')
    list_filter = ('reported_at',)
    search_fields = ('reason', 'reporter__username', 'message__message')
