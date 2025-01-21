from django.urls import path
from .views import PrinterList

urlpatterns = [
    path('api/printers/', PrinterList.as_view(), name='printer-list'),
]
