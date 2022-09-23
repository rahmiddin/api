
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer


class SensorView(APIView):

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('ok')
        return Response('JSON not valid')

    def patch(self, request):
        serializer = SensorSerializer(data=request.data)
        instance = Sensor.objects.get(pk=request.data.get('id'))
        if serializer.is_valid():
            serializer.update(instance=instance, validated_data=request.data)
            return Response('ok')
        return Response('JSON not valid')

    def get(self, request):
        data = Sensor.objects.all()
        serializer = SensorSerializer(instance=data, many=True)
        print(serializer)
        return Response(serializer.data)


class MeasurementView(APIView):

    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.create(validated_data=request.data)
            return Response('ok')
        return Response('JSON not valid')

