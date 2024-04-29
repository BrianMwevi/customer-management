from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

SUPER_USERS = ['JAMBOPAY', 'MANAGEMENT']


class UserLevel(models.TextChoices):
    JAMBOPAY = "JAMBOPAY", _('JAMBOPAY')
    MANAGEMENT = "MANAGEMENT", _('MANAGEMENT')
    STAFF = "STAFF", _('STAFF')


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise TypeError(_('User must have a email'))
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        if password is None:
            raise TypeError('User must have a password')

        if extra_fields.get('level') not in SUPER_USERS:
            raise TypeError('User must have a password')

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_verified', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    phone = models.CharField(max_length=255, unique=True, db_index=True, blank=True, null=True)
    username = None
    level = models.CharField(max_length=256, choices=UserLevel.choices, default=UserLevel.STAFF)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('level',)

    objects = UserManager()

    def __str__(self):
        return self.email


class UserInvite(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
