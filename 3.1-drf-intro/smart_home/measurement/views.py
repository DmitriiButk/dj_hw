from .models import Measurement, Sensor
from .serializers import SensorDetailSerializer, MeasurementSerializer, SensorSerializer
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView


class SensorsViewAndCreate(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementUpdateView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorViewAndUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer