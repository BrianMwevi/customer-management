from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.configs.swagger')),
    path('api/customers/', include('src.customer.urls')),
    path('api/locations/', include('src.location.urls')),
]
