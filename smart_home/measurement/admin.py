from django.contrib import admin
from .models import Sensor, Measurement
# Register your models here.


@admin.register(Sensor)
class SensorView(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Measurement)
class SensorView(admin.ModelAdmin):
    list_display = ['sensor_id', 'temp', 'date']
