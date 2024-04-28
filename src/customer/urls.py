from django.urls import path

from src.customer.views import (
    BusinessCategoryListCreateView, BusinessCategoryRetrieveUpdateView,
    BusinessListCreateView, BusinessRetrieveUpdateView,
    CustomerListCreateView, CustomerRetrieveUpdateView
)

urlpatterns = [

    path('business-categories', BusinessCategoryListCreateView.as_view(), name='business-categories-list-create'),
    path('business-categories/<int:pk>', BusinessCategoryRetrieveUpdateView.as_view(), name='business-categories'
                                                                                            '-retrieve-update'),
    path('business', BusinessListCreateView.as_view(), name='business-list-create'),
    path('business/<int:pk>', BusinessRetrieveUpdateView.as_view(), name='business-retrieve-update'),
    path('customers', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>', CustomerRetrieveUpdateView.as_view(), name='customer-retrieve-update'),
]
