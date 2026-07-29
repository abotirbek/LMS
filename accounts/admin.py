from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, TeacherProfile, StudentProfile


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "role",
        "phone",
        "is_staff",
        "is_active",
    )

    list_filter = (
        "role",
        "is_staff",
        "is_superuser",
        "is_active",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional Information",
            {
                "fields": (
                    "role",
                    "phone",
                    "avatar",
                )
            },
        ),
    )


@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "specialization",
        "created_at",
    )
    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "specialization",
    )


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "birth_date",
        "parent_phone",
        "coin_balance",
        "created_at",
    )
    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
    )