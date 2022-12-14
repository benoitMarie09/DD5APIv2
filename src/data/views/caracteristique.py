from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
 
from data.models import Caracteristique
from data.serializers import CaracteristiqueListSerializers, CaracteristiqueDetailSerializers
 

class CaracteristiqueViewset(ReadOnlyModelViewSet):

    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = Caracteristique
    serializer_classes = {
        'list':CaracteristiqueListSerializers,
        'retrieve':CaracteristiqueDetailSerializers,
    }

    default_serializer_class = CaracteristiqueListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return Caracteristique.objects.all()