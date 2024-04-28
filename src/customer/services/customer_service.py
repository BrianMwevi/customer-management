from django.db.models import QuerySet

from src.customer.models import BusinessCategory, Business, Customer


class CustomerService:

    @staticmethod
    def create_business_category(**kwargs) -> BusinessCategory:
        return BusinessCategory.objects.create(**kwargs)

    @staticmethod
    def filter_business_categories(**kwargs) -> QuerySet[BusinessCategory]:
        return BusinessCategory.objects.filter(**kwargs)

    @staticmethod
    def create_business(**kwargs) -> Business:
        return Business.objects.create(**kwargs)

    @staticmethod
    def filter_businesses(**kwargs) -> QuerySet[Business]:
        return Business.objects.filter(**kwargs)

    @staticmethod
    def create_customer(**kwargs) -> Customer:
        return Customer.objects.create(**kwargs)

    @staticmethod
    def filter_customers(**kwargs) -> QuerySet[Customer]:
        return Customer.objects.filter(**kwargs)
