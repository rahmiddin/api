from django.db import models


class Sensor(models.Model):
    name = models.CharField(null=False, max_length=50)
    descriptions = models.CharField(max_length=250)

    class Meta():
        verbose_name = 'Датчик'

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temp = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)