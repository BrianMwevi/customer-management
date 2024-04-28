from django.urls import path

from src.location.views import (
    CountyListCreateView, CountyRetrieveUpdateView,
    SubCountyListCreateView, SubCountyRetrieveUpdateView,
    WardListCreateView, WardRetrieveUpdateView)


urlpatterns = [
    path('counties', CountyListCreateView.as_view(), name='county-list-create'),
    path('counties/<int:pk>', CountyRetrieveUpdateView.as_view(), name='county-retrieve-update'),
    path('sub-counties', SubCountyListCreateView.as_view(), name='sub-county-list-create'),
    path('sub-counties/<int:pk>', SubCountyRetrieveUpdateView.as_view(), name='sub-county-retrieve-update'),
    path('wards', WardListCreateView.as_view(), name='ward-list-create'),
    path('wards/<int:pk>', WardRetrieveUpdateView.as_view(), name='ward-retrieve-update'),
]