from django.core.management.base import BaseCommand
from printers.models import Printer
from printers.utils import get_printer_toner_level

class Command(BaseCommand):
    help = "Updates the toner levels of all printers"

    def handle(self, *args, **kwargs):
        printers = Printer.objects.all()
        for printer in printers:
            toner_levels = get_printer_toner_level(printer.ip_address)

            if toner_levels:
                printer.toner_black = toner_levels.get('black', printer.toner_black)
                printer.toner_cyan = toner_levels.get('cyan', printer.toner_cyan)
                printer.toner_magenta = toner_levels.get('magenta', printer.toner_magenta)
                printer.toner_yellow = toner_levels.get('yellow', printer.toner_yellow)
                printer.save()

                self.stdout.write(f"Updated {printer.name} to black: {printer.toner_black}%, cyan: {printer.toner_cyan}%, magenta: {printer.toner_magenta}%, yellow: {printer.toner_yellow}%")
            else:
                self.stdout.write(f"Failed to update toner levels for {printer.name}")
