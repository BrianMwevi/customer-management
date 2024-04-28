from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.configs.swagger')),
    path('customers/', include('src.customer.urls')),
    path('locations/', include('src.location.urls')),
]
