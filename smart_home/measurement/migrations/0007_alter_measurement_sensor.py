# Generated by Django 4.1.1 on 2022-09-23 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0006_alter_measurement_sensor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor'),
        ),
    ]
