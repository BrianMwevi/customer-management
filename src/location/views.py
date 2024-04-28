from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from src.location.location_service import LocationService

from src.location import location_serializer


class CountyListCreateView(ListCreateAPIView):
    queryset = LocationService.filter_counties()
    serializer_class = location_serializer.CountySerializer


class CountyRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = LocationService.filter_counties()
    serializer_class = location_serializer.CountySerializer


class SubCountyListCreateView(ListCreateAPIView):
    queryset = LocationService.filter_counties()
    serializer_class = location_serializer.SubCountySerializer


class SubCountyRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = LocationService.filter_counties()
    serializer_class = location_serializer.SubCountySerializer


class WardListCreateView(ListCreateAPIView):
    queryset = LocationService.filter_counties()
    serializer_class = location_serializer.WardSerializer


class WardRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = LocationService.filter_wards()
    serializer_class = location_serializer.WardSerializer


class LocationListCreateView(ListCreateAPIView):
    queryset = LocationService.filter_counties()
    serializer_class = location_serializer.LocationSerializer


class LocationRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = LocationService.filter_counties()
    serializer_class = location_serializer.LocationSerializer
