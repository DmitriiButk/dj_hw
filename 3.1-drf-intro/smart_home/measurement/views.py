from .models import Measurement, Sensor
from .serializers import SensorDetailSerializer, MeasurementSerializer, SensorSerializer, \
    SensorUpdateSerializer, MeasurementUpdateSerializer
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, RetrieveAPIView


class SensorsViewAndCreate(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class MeasurementUpdateView(ListCreateAPIView):
    serializer_class = MeasurementUpdateSerializer


class SensorViewAndUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, *args, **kwargs):
        serializer = SensorDetailSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return super().patch(request)
