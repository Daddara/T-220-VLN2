from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Payment(models.Model):
    card_number = models.IntegerField(validators=[RegexValidator(regex='^.{16}$', message='Length has to be 16')])
    card_cvc = models.IntegerField(validators=[RegexValidator(regex='^.{3}$', message='Length has to be 3')])
    card_expire_year = models.IntegerField(validators=[RegexValidator(regex='^.{2}$', message='Length has to be 2')])
    card_expire_month = models.IntegerField(validators=[RegexValidator(regex='^.{2}$', message='Length has to be 2')] )
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    house_number = models.CharField(max_length=4)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=4)
