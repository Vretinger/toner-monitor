from django.core.management.base import BaseCommand
from printers.models import Printer
from printers.utils import get_printer_toner_level

class Command(BaseCommand):
    help = "Updates the toner levels of all printers"

    def handle(self, *args, **kwargs):
        printers = Printer.objects.all()
        for printer in printers:
            toner_level = get_printer_toner_level(printer.ip_address)
            if toner_level is not None:
                printer.toner_level = toner_level
                printer.save()
                self.stdout.write(f"Updated {printer.name} to {toner_level}%")
            else:
                self.stdout.write(f"Failed to update {printer.name}")
