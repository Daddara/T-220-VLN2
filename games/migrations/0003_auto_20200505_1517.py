# Generated by Django 3.0.6 on 2020-05-05 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20200505_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='console',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
