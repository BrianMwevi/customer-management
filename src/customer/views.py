from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from src.customer.serializers import customer_serializer
from src.customer.services.customer_service import CustomerService


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
    permission_classes = ()
    authentication_classes = ()
    queryset = CustomerService.filter_customers()
    serializer_class = customer_serializer.CustomerSerializer


class CustomerRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = CustomerService.filter_customers()
    serializer_class = customer_serializer.CustomerSerializer
