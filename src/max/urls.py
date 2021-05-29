from django.contrib import admin
from django.urls import path

from orders.views import orderManagement

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',orderManagement)
]
