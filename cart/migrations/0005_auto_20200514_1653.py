# Generated by Django 3.0.6 on 2020-05-14 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20200514_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]