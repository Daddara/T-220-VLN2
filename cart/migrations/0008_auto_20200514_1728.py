# Generated by Django 3.0.6 on 2020-05-14 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_auto_20200514_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
    ]