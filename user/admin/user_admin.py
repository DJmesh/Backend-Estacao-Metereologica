from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_active", "is_staff", "date_joined")
    list_filter = ("is_active", "is_staff", "is_superuser", "groups")
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("username",)
    readonly_fields = ("last_login", "date_joined")
    fieldsets = (
        ("Credenciais", {"fields": ("username", "password")}),
        ("Dados pessoais", {"fields": ("first_name", "last_name", "email")}),
        ("Permissões", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Datas", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "is_active", "is_staff"),
        }),
    )
    save_on_top = True
