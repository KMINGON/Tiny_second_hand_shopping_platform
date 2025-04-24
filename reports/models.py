from django.db import models
from accounts.models import CustomUser
from chat.models import Chat

class UserReport(models.Model):
    reporter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reported_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reported')
    reason = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('reporter', 'reported_user')

class ChatReport(models.Model):
    reporter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.ForeignKey(Chat, on_delete=models.CASCADE)
    reason = models.TextField(blank=True)
    reported_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('reporter', 'message')  # 동일 사용자의 중복 신고 방지
