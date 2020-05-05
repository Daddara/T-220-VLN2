from django.db import models


# Create your models here.

class Consoles(models.Model):
    name = models.CharField(max_length=999, blank=True)
    image = models.CharField(max_length=999, blank=True)
    release_date = models.DateField(blank=True)
    description = models.CharField(max_length=99999, blank=True)
    price = models.FloatField(blank=True)

    def __str__(self):
        return self.name
