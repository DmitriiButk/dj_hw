from django.urls import path
from .views import MeasurementUpdateView, SensorViewAndUpdate, SensorsViewAndCreate

urlpatterns = [
    path('sensor/', SensorsViewAndCreate.as_view()),
    path('measure/', MeasurementUpdateView.as_view())
]
