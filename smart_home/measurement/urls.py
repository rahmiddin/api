from django.urls import path
from .views import SensorView, MeasurementView

urlpatterns = [
    path('sensor/', SensorView.as_view()),
    path('measurement/', MeasurementView.as_view())
]
