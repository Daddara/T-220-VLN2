from django.db import models
from consoles.models import Consoles


# Create your models here.

class Games(models.Model):
    name = models.CharField(max_length=999, blank=True)
    image = models.CharField(max_length=999, blank=True)
    release_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=9999, blank=True)
    price = models.FloatField(blank=True)
    console = models.ForeignKey(Consoles, on_delete=models.CASCADE)


    def __str__(self):
        return self.name