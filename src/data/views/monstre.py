from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from data.models import Monstre, CapaciteMonstre
from data.serializers import MonstreSerializers, CapaciteMonstreSerializers

 
 
class MonstreViewset(ReadOnlyModelViewSet):

    serializer_class = MonstreSerializers

    def get_queryset(self):
        return Monstre.objects.all()
 

class CapaciteMonstreViewset(ReadOnlyModelViewSet):

    serializer_class = CapaciteMonstreSerializers

    def get_queryset(self):
        return CapaciteMonstre.objects.all()