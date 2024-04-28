from rest_framework import serializers

from src.location.models import County, SubCounty, Ward, Location


class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = '__all__'


class SubCountySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCounty
        fields = '__all__'


class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
