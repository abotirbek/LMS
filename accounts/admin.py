from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'get_full_name', 'role', 'phone']
    list_filter = ['role']
    fieldsets = UserAdmin.fieldsets + (
        ("Qo'shimcha", {'fields': ('role', 'phone', 'avatar')}),
    )