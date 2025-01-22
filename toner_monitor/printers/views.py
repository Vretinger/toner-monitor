from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import Printer
from .serializers import PrinterSerializer
from rest_framework import viewsets

class PrinterViewSet(viewsets.ModelViewSet):
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer

class PrinterList(APIView):
    def get(self, request):
        printers = Printer.objects.all()
        serializer = PrinterSerializer(printers, many=True)
        return Response(serializer.data)

def index(request):
    return render(request, 'index.html')