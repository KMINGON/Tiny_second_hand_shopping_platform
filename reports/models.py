from django.db import models
from accounts.models import CustomUser
from chat.models import Chat
from products.models import Product

__all__ = ['UserReport', 'ChatReport', 'ProductReport']

class UserReport(models.Model):
    reporter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reported_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reported')
    reason = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('reporter', 'reported_user')  # 중복 신고 방지

    def __str__(self):
        return f"{self.reporter.username} → {self.reported_user.username}"

class ChatReport(models.Model):
    reporter = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reports_chatreport')
    message = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='reports_chatreport')
    reason = models.TextField(blank=True)
    reported_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('reporter', 'message')  # 동일 사용자의 중복 신고 방지

class ProductReport(models.Model):
    reporter = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reports_productreport')
    reported_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reports')
    reason = models.TextField(blank=True)
    reported_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('reporter', 'reported_product')

    def __str__(self):
        return f"{self.reporter.username} → {self.reported_product.name}"