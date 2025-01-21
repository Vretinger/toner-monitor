from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Printer
from .serializers import PrinterSerializer


class PrinterViewSet(ModelViewSet):
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer

def index(request):
    return render(request, 'index.html')