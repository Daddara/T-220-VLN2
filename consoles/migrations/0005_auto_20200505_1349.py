# Generated by Django 3.0.6 on 2020-05-05 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consoles', '0004_auto_20200505_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consoles',
            name='name',
            field=models.CharField(blank=True, max_length=999),
        ),
        migrations.AlterField(
            model_name='consoles',
            name='price',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='consoles',
            name='release_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
