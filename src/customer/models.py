from django.db import models
from django.utils import timezone

from src.location.models import Ward
from src.utils.models import TimeStamped


class BusinessCategory(TimeStamped):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Business(TimeStamped):
    business_name = models.CharField(max_length=100)
    building_name = models.CharField(max_length=100)
    floor = models.CharField(max_length=255, blank=True, null=True)
    registration_date = models.DateField()
    category = models.ForeignKey(BusinessCategory, on_delete=models.CASCADE, related_name='category_businesses')
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, related_name='locations', null=True)

    @property
    def age(self):
        today = timezone.now().date()
        return (today - self.registration_date).days // 365


class Customer(TimeStamped):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)


class BusinessCustomer(TimeStamped):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='businesses')
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='customers')

    class Meta:
        unique_together = ('customer', 'business')
