from django.urls import path

from src.customer.views import (
    BusinessCategoryListCreateView, BusinessCategoryRetrieveUpdateView,
    BusinessListView, BusinessRetrieveUpdateView,
    CustomerListView, CustomerRetrieveUpdateView,
    BusinessCustomerListCreateView, BusinessCustomerRetrieveUpdateView,
)

urlpatterns = [

    path('business-categories', BusinessCategoryListCreateView.as_view(), name='business-categories-list-create'),
    path('business-categories/<int:pk>', BusinessCategoryRetrieveUpdateView.as_view(), name='business-categories'
                                                                                            '-retrieve-update'),
    path('business', BusinessListView.as_view(), name='business-list-create'),
    path('business/<int:pk>', BusinessRetrieveUpdateView.as_view(), name='business-retrieve-update'),
    path('customers', CustomerListView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>', CustomerRetrieveUpdateView.as_view(), name='customer-retrieve-update'),
    path('business-customer', BusinessCustomerListCreateView.as_view(), name='business-customer-list-create'),
    path('business-customer/<int:pk>', BusinessCustomerRetrieveUpdateView.as_view(), name='business-customer-retrieve-update'),
]
