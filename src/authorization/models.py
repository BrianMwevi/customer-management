from django.db import models
from django.utils.translation import gettext_lazy as _

from src.authentication.models import User
from src.utils.models import TimeStamped


class RoleLevels(models.TextChoices):
    JAMBOPAY_ADMIN = "JAMBOPAY_ADMIN", _('Jambopay Admin')
    CUSTOMER_MANAGEMENT = "CUSTOMER_MANAGEMENT", _('Customer Management')
    STAFF = "STAFF", _('Staff')


class Role(TimeStamped):
    name = models.CharField(max_length=256)
    status = models.BooleanField(default=True)
    level = models.CharField(max_length=256, choices=RoleLevels.choices)

    def __str__(self):
        return self.name


class UserRole(TimeStamped):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
