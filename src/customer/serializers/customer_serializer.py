from rest_framework import serializers
from src.customer.models import BusinessCategory, Business, Customer, BusinessCustomer


class BusinessCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCategory
        fields = '__all__'


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class BusinessCustomerSerializer(serializers.ModelSerializer):
    business = BusinessSerializer()
    customer = CustomerSerializer()

    class Meta:
        model = BusinessCustomer
        fields = '__all__'
