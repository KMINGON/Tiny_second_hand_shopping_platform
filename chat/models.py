from django.db import models
from accounts.models import CustomUser

class Chat(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_messages', on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

class ChatReport(models.Model):
    reporter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.ForeignKey(Chat, on_delete=models.CASCADE)
    reason = models.TextField(blank=True)
    reported_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('reporter', 'message')  # 동일 사용자의 중복 신고 방지
