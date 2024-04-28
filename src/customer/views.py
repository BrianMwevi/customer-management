from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.response import Response

from src.customer.serializers import customer_serializer
from src.customer.services.customer_service import CustomerService


class BusinessCategoryListCreateView(ListCreateAPIView):
    queryset = CustomerService.filter_business_categories()
    serializer_class = customer_serializer.BusinessCategorySerializer


class BusinessCategoryRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = CustomerService.filter_business_categories()
    serializer_class = customer_serializer.BusinessCategorySerializer


class BusinessListView(ListAPIView):
    queryset = CustomerService.filter_businesses()
    serializer_class = customer_serializer.BusinessSerializer


class BusinessRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = CustomerService.filter_businesses()
    serializer_class = customer_serializer.BusinessSerializer


class CustomerListView(ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = CustomerService.filter_customers()
    serializer_class = customer_serializer.CustomerSerializer


class CustomerRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = CustomerService.filter_customers()
    serializer_class = customer_serializer.CustomerSerializer


class BusinessCustomerListCreateView(ListCreateAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = CustomerService.filter_customers()
    serializer_class = customer_serializer.BusinessCustomerSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customer = CustomerService.create_customer(**serializer.validated_data.get('customer'))
        business = CustomerService.create_business(**serializer.validated_data.get('business'))
        business_customer = CustomerService.create_business_customer(customer=customer, business=business)
        serialized_response = self.get_serializer(business_customer)
        return Response(data=serialized_response.data, status=status.HTTP_201_CREATED)



class BusinessCustomerRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = CustomerService.filter_customers()
    serializer_class = customer_serializer.BusinessCustomerSerializer

