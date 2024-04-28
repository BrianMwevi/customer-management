from django.urls import path

from src.customer.views import (
    CountyListCreateView, CountyRetrieveUpdateView,
    SubCountyListCreateView, SubCountyRetrieveUpdateView,
    WardListCreateView, WardRetrieveUpdateView,
    BusinessCategoryListCreateView, BusinessCategoryRetrieveUpdateView,
    BusinessListCreateView, BusinessRetrieveUpdateView,
    CustomerListCreateView, CustomerRetrieveUpdateView
)

urlpatterns = [
    path('counties', CountyListCreateView.as_view(), name='county-list-create'),
    path('counties/<int:pk>', CountyRetrieveUpdateView.as_view(), name='county-retrieve-update'),
    path('sub-counties', SubCountyListCreateView.as_view(), name='sub-county-list-create'),
    path('sub-counties/<int:pk>', SubCountyRetrieveUpdateView.as_view(), name='sub-county-retrieve-update'),
    path('wards', WardListCreateView.as_view(), name='ward-list-create'),
    path('wards/<int:pk>', WardRetrieveUpdateView.as_view(), name='ward-retrieve-update'),
    path('business-categories', BusinessCategoryListCreateView.as_view(), name='business-categories-list-create'),
    path('business-categories/<int:pk>', BusinessCategoryRetrieveUpdateView.as_view(), name='business-categories'
                                                                                            '-retrieve-update'),
    path('business', BusinessListCreateView.as_view(), name='business-list-create'),
    path('business/<int:pk>', BusinessRetrieveUpdateView.as_view(), name='business-retrieve-update'),
    path('customers', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>', CustomerRetrieveUpdateView.as_view(), name='customer-retrieve-update'),
]
