from django.contrib import admin

from .models import BusinessCategory, Business, Customer, BusinessCustomer


def get_model_fields(model):
    fields = model._meta.fields
    return [field.name for field in fields], [field.name for field in fields]


@admin.register(BusinessCategory)
class BusinessCategoryAdmin(admin.ModelAdmin):
    list_display, search_fields = get_model_fields(BusinessCategory)


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display, search_fields = get_model_fields(Business)
    list_display += ['age']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display, search_fields = get_model_fields(Customer)


@admin.register(BusinessCustomer)
class BusinessCustomerAdmin(admin.ModelAdmin):
    list_display, search_fields = get_model_fields(BusinessCustomer)
