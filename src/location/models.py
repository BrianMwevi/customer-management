from django.db import models

from src.utils.models import TimeStamped


class County(TimeStamped):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Counties'


class SubCounty(TimeStamped):
    name = models.CharField(max_length=100)
    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name='sub_counties')

    class Meta:
        verbose_name_plural = 'Sub-counties'


class Ward(TimeStamped):
    name = models.CharField(max_length=100)
    sub_county = models.ForeignKey(SubCounty, on_delete=models.CASCADE, related_name='wards')
