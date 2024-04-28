from rest_framework import serializers
from src.customer.models import BusinessCategory, Business, Customer
from src.location.location_serializer import LocationSerializer


class BusinessCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCategory
        fields = '__all__'


class BusinessSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Business
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    business = BusinessSerializer()

    class Meta:
        model = Customer
        fields = '__all__'
