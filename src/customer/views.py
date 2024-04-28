from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from src.customer.serializers import customer_serializer
from src.customer.services.customer_service import CustomerService


class CountyListCreateView(ListCreateAPIView):
    queryset = CustomerService.filter_counties()
    serializer_class = customer_serializer.CountySerializer


class CountyRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = CustomerService.filter_counties()
    serializer_class = customer_serializer.CountySerializer


class SubCountyListCreateView(ListCreateAPIView):
    queryset = CustomerService.filter_counties()
    serializer_class = customer_serializer.SubCountySerializer


class SubCountyRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = CustomerService.filter_counties()
    serializer_class = customer_serializer.SubCountySerializer


class WardListCreateView(ListCreateAPIView):
    queryset = CustomerService.filter_counties()
    serializer_class = customer_serializer.WardSerializer


class WardRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = CustomerService.filter_wards()
    serializer_class = customer_serializer.WardSerializer


class LocationListCreateView(ListCreateAPIView):
    queryset = CustomerService.filter_counties()
    serializer_class = customer_serializer.LocationSerializer


class LocationRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = CustomerService.filter_counties()
    serializer_class = customer_serializer.LocationSerializer


class BusinessCategoryListCreateView(ListCreateAPIView):
    queryset = CustomerService.filter_business_categories()
    serializer_class = customer_serializer.BusinessCategorySerializer


class BusinessCategoryRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = CustomerService.filter_business_categories()
    serializer_class = customer_serializer.BusinessCategorySerializer


class BusinessListCreateView(ListCreateAPIView):
    queryset = CustomerService.filter_businesses()
    serializer_class = customer_serializer.BusinessSerializer


class BusinessRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = CustomerService.filter_businesses()
    serializer_class = customer_serializer.BusinessSerializer


class CustomerListCreateView(ListCreateAPIView):
    queryset = CustomerService.filter_customers()
    serializer_class = customer_serializer.CustomerSerializer


class CustomerRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = CustomerService.filter_customers()
    serializer_class = customer_serializer.CustomerSerializer
