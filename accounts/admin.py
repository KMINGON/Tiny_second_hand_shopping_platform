from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_active', 'is_admin']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'account_number', 'is_admin')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)