from django.db import models
from django.utils import timezone
from src.utils.models import TimeStamped


class County(TimeStamped):
    name = models.CharField(max_length=100)


class SubCounty(TimeStamped):
    name = models.CharField(max_length=100)
    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name='sub_counties')


class Ward(TimeStamped):
    name = models.CharField(max_length=100)
    sub_county = models.ForeignKey(SubCounty, on_delete=models.CASCADE, related_name='wards')


class Location(TimeStamped):
    building_name = models.CharField(max_length=100)
    floor = models.CharField(max_length=255, blank=True, null=True)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, related_name='locations')


class BusinessCategory(TimeStamped):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Business(TimeStamped):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(BusinessCategory, on_delete=models.CASCADE, related_name='category_businesses')
    registration_date = models.DateField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='location_businesses')

    @property
    def age(self):
        today = timezone.now().date()
        return (today - self.registration_date).days // 365


class Customer(TimeStamped):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='customers')