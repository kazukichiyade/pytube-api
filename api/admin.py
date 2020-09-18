from django.contrib import admin
from .models import Video, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _


# BaseUserAdminのuserNameからemailに変える為オーバーライドする
class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["email", "username"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("username",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )


# モデルを指定する事でadminダッシュボードで利用する事ができる
admin.site.register(User, UserAdmin)

admin.site.register(Video)
