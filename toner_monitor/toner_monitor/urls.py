from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from printers.views import PrinterViewSet, index



router = DefaultRouter()
router.register(r'printers', PrinterViewSet, basename='printer')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', index, name='index'),
]
