# Generated by Django 3.0.6 on 2020-05-14 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_auto_20200514_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
