from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    account_number = models.CharField(max_length=30, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
