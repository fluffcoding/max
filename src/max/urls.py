from django.contrib import admin
from django.urls import path

from orders.views import orderManagement,modal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',orderManagement),
    path('modal',modal),
]
