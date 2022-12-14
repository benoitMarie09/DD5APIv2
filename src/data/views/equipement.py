from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
 
from data.models import Equipement, CategorieEquipement, Arme, Armure, ProprieteArme, Vehicule
from data.serializers import ProprieteArmeDetailSerializers, ProprieteArmeListSerializers, VehiculeDetailSerializers, VehiculeListSerializers, EquipementListSerializers, EquipementDetailSerializers, CategorieEquipementListSerializers, CategorieEquipementDetailSerializers, ArmeListSerializers, ArmeDetailSerializers, ArmureDetailSerializers, ArmureListSerializers

 
class EquipementViewset(ReadOnlyModelViewSet):

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categorie_equipement',]

    model = Equipement
    serializer_classes = {
        'list':EquipementListSerializers,
        'retrieve':EquipementDetailSerializers,
    }

    default_serializer_class = EquipementListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return Equipement.objects.select_subclasses()
 
class CategorieEquipementViewset(ReadOnlyModelViewSet):

    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = CategorieEquipement
    serializer_classes = {
        'list':CategorieEquipementListSerializers,
        'retrieve':CategorieEquipementDetailSerializers,
    }

    default_serializer_class = CategorieEquipementListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return CategorieEquipement.objects.all()
 

class ProprieteArmeViewset(ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = ProprieteArme
    serializer_classes = {
        'list':ProprieteArmeListSerializers,
        'retrieve':ProprieteArmeDetailSerializers,
    }

    default_serializer_class = ProprieteArmeListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return ProprieteArme.objects.all()