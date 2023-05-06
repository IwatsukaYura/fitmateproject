from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# from . models import CustomUser
CustomUser = get_user_model()



class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("age","height", "weight","target_weight")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username","email", "height", "weight","target_weight", "password1", "password2"),
            },
        ),
    )

    list_display = ("username","email", "height", "weight", "is_staff")
    list_filter = ("is_staff", "is_superuser", "groups")
    search_fields = ("email", "email")
    ordering = ("height",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )

admin.site.register(CustomUser, CustomUserAdmin)