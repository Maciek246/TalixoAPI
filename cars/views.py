from rest_framework.viewsets import ModelViewSet

from .models import Car
from .serializers import CarSerializer, CarCreateSerializer


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CarSerializer
        return CarCreateSerializer

