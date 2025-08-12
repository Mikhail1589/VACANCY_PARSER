from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import ProjectUser


# UserAdmin.fieldsets += (
#     ('Extra Fields', {'fields': ('bio',)}),
# )
# Регистрируем модель в админке:
admin.site.register(ProjectUser, UserAdmin)
