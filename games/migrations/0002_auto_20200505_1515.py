# Generated by Django 3.0.6 on 2020-05-05 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consoles', '0008_auto_20200505_1436'),
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='console',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consoles.Consoles'),
        ),
    ]
