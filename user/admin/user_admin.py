from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from user.models.user import User

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = ("username", "email", "is_staff", "is_active", "date_joined")
    search_fields = ("username", "email")
    ordering = ("username",)

    # Exibir o guid em readonly
    readonly_fields = ("guid",)
    fieldsets = DjangoUserAdmin.fieldsets + (
        ("Identificação", {"fields": ("guid",)}),
    )
