# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics, status
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class ListCreateSensorsView(generics.ListCreateAPIView):
    # list of sensors plus create a new sensor
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class AddMeasurementView(generics.CreateAPIView):
    # add measurement
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class ReadChangeSensorView(generics.RetrieveUpdateAPIView):
    # read or change a sensor (description and/or name)
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


    # def get_queryset(self):
    #     sensor = self.request.data
    #
    #     queryset = Sensor.ob



