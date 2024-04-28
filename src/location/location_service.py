from django.db.models import QuerySet

from src.location.models import County, SubCounty, Ward


class LocationService:
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

