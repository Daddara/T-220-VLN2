from django.db import models


# Create your models here.

class Consoles(models.Model):
    name = models.CharField(max_length=255)
    # description = models.CharField(max_length=999, blank=True)
    # logo = models.CharField(max_length=999, blank=True)
    # year_created = models.DateTimeField(null=True)
    price = models.FloatField()

    def __str__(self):
        return self.name
