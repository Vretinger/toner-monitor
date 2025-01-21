from django.db import models

class Printer(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    toner_black = models.IntegerField(default=100)
    toner_cyan = models.IntegerField(default=100)
    toner_magenta = models.IntegerField(default=100)
    toner_yellow = models.IntegerField(default=100)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name