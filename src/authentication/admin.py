from django.contrib import admin
from .models import User, UserInvite

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]
    search_fields = [field.name for field in User._meta.fields]

@admin.register(UserInvite)
class UserInviteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserInvite._meta.fields]
    search_fields = [field.name for field in UserInvite._meta.fields]

