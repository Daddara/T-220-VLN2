from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from consoles.models import Consoles
from games.models import Games


class Cart(models.Model):
    u = models.ForeignKey(User,  on_delete=models.CASCADE)
    game = models.ForeignKey(Games, on_delete=models.CASCADE, blank=True, null=True)
    console = models.ForeignKey(Consoles, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.DecimalField(max_digits=3, decimal_places=2)  # 1

