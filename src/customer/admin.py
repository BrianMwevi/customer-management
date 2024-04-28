from django.contrib import admin

from .models import County, SubCounty, Ward, Location, BusinessCategory, Business, Customer


def get_model_fields(model):
    fields = model._meta.fields
    return [field.name for field in fields], [field.name for field in fields]


@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display, search_fields = get_model_fields(County)


@admin.register(SubCounty)
class SubCountyAdmin(admin.ModelAdmin):
    list_display, search_fields = get_model_fields(SubCounty)


@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display, search_fields = get_model_fields(Ward)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display, search_fields = get_model_fields(Location)


@admin.register(BusinessCategory)
class BusinessCategoryAdmin(admin.ModelAdmin):
    list_display, search_fields = get_model_fields(BusinessCategory)


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display, search_fields = get_model_fields(Business)
    list_display += ['age']  # Add the 'age' property to the list display


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display, search_fields = get_model_fields(Customer)