# Generated by Django 3.0.6 on 2020-05-14 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]