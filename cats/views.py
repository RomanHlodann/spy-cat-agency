from rest_framework import viewsets

from cats.models import Cat
from cats.serializers import CatSerializer, CatUpdateSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    def get_serializer_class(self):
        if self.action == 'update':
            return CatUpdateSerializer

        return self.serializer_class
