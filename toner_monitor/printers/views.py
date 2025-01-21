from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Printer
from .serializers import PrinterSerializer

class PrinterList(APIView):
    def get(self, request):
        printers = Printer.objects.all()
        serializer = PrinterSerializer(printers, many=True)
        return Response(serializer.data)
