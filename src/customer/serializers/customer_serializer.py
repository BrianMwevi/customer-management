from rest_framework import serializers
from src.customer.models import BusinessCategory, Business, Customer


class BusinessCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCategory
        fields = '__all__'


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    business = BusinessSerializer()

    class Meta:
        model = Customer
        fields = '__all__'
