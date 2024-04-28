from django.db import models

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
