from django.contrib import admin

from src.authorization.models import UserRole, Role


def get_model_fields(model):
    fields = model._meta.fields
    return [field.name for field in fields], [field.name for field in fields]


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display, search_fields = get_model_fields(Role)


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display, search_fields = get_model_fields(UserRole)

