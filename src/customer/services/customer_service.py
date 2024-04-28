from django.db.models import QuerySet

from src.customer.models import County, SubCounty, Ward, Location, BusinessCategory, Business, Customer


class CustomerService:

    @staticmethod
    def create_county(**kwargs) -> County:
        return County.objects.create(**kwargs)

    @staticmethod
    def filter_counties(**kwargs) -> QuerySet[County]:
        return County.objects.filter(**kwargs)

    @staticmethod
    def create_sub_county(**kwargs) -> SubCounty:
        return SubCounty.objects.create(**kwargs)

    @staticmethod
    def filter_sub_counties(**kwargs) -> QuerySet[SubCounty]:
        return SubCounty.objects.filter(**kwargs)

    @staticmethod
    def create_ward(**kwargs) -> Ward:
        return Ward.objects.create(**kwargs)

    @staticmethod
    def filter_wards(**kwargs) -> QuerySet[Ward]:
        return Ward.objects.filter(**kwargs)

    @staticmethod
    def create_location(**kwargs) -> Location:
        return Location.objects.create(**kwargs)

    @staticmethod
    def filter_locations(**kwargs) -> QuerySet[Location]:
        return Location.objects.filter(**kwargs)

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
