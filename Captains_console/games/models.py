from django.db import models
# from consoles.models import Consoles


# Create your models here.

class Games(models.Model):
    name = models.CharField(max_length=255)
    # description = models.CharField(max_length=999, blank=True)
    # console = models.ForeignKey(Consoles, on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return self.name