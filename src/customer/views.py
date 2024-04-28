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

