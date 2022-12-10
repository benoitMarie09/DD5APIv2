from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
 
from .models import *
from .serializers_details import *
from .serializers_lists import *
 

class RaceViewset(ReadOnlyModelViewSet):

    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = Race
    serializer_classes = {
        'list':RaceListSerializers,
        'retrieve':RaceDetailSerializers,
    }

    default_serializer_class = RaceListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return Race.objects.filter(parent_race=True).select_subclasses()

class SousRaceViewset(ReadOnlyModelViewSet):

    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = SousRace
    serializer_classes = {
        'list':SousRaceListSerializers,
        'retrieve':SousRaceDetailSerializers,
    }

    default_serializer_class = SousRaceListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return SousRace.objects.all()
 
class MaitriseViewset(ReadOnlyModelViewSet):

    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = Maitrise
    serializer_classes = {
        'list':MaitriseListSerializers,
        'retrieve':MaitriseDetailSerializers,
    }

    default_serializer_class = MaitriseListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return Maitrise.objects.all()
 
class LangueViewset(ReadOnlyModelViewSet):

    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = Langue
    serializer_classes = {
        'list':LangueListSerializers,
        'retrieve':LangueDetailSerializers,
    }

    default_serializer_class = LangueListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return Langue.objects.all()
 
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
 
class TraitViewset(ReadOnlyModelViewSet):

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['race']

    model = Trait
    serializer_classes = {
        'list':TraitListSerializers,
        'retrieve':TraitDetailSerializers,
    }

    default_serializer_class = TraitListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return Trait.objects.all()

class SortViewset(ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = Sort
    serializer_classes = {
        'list':SortListSerializers,
        'retrieve':SortDetailSerializers,
    }

    default_serializer_class = SortListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return Sort.objects.all()

class AlignementViewset(ReadOnlyModelViewSet):

    serializer_class = AlignementSerializers

    def get_queryset(self):
        return Alignement.objects.all()
 
class HistoriqueViewset(ReadOnlyModelViewSet):

    serializer_class = HistoriqueSerializers

    def get_queryset(self):
        return Historique.objects.all()
 
class EquipementViewset(ReadOnlyModelViewSet):

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categorie_equipement',]

    model = Arme
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
 
class ArmeViewset(ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categorie_arme', 'type_portee',]

    model = Arme
    serializer_classes = {
        'list':ArmeListSerializers,
        'retrieve':ArmeDetailSerializers,
    }

    default_serializer_class = ArmeListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return Arme.objects.all()

     
class ArmureViewset(ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categorie_armure',]

    model = Armure
    serializer_classes = {
        'list':ArmureListSerializers,
        'retrieve':ArmureDetailSerializers,
    }

    default_serializer_class = ArmureListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return Armure.objects.all()
 
# class PackEquipementViewset(ReadOnlyModelViewSet):

#     serializer_class = PackEquipementSerializers

#     def get_queryset(self):
#         return PackEquipement.objects.all()
 
class VehiculeViewset(ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = Vehicule
    serializer_classes = {
        'list':VehiculeListSerializers,
        'retrieve':VehiculeDetailSerializers,
    }

    default_serializer_class = VehiculeListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return Vehicule.objects.all()
 
class ProprieteArmeViewset(ReadOnlyModelViewSet):

    serializer_class = ProprieteArmeSerializers

    def get_queryset(self):
        return ProprieteArme.objects.all()
 
class TypeDegatViewset(ReadOnlyModelViewSet):

    serializer_class = TypeDegatSerializers

    def get_queryset(self):
        return TypeDegat.objects.all()
 
class ClasseViewset(ReadOnlyModelViewSet):

    serializer_class = ClasseSerializers

    def get_queryset(self):
        return Classe.objects.all()
 
class IncantationViewset(ReadOnlyModelViewSet):

    serializer_class = IncantationSerializers

    def get_queryset(self):
        return Incantation.objects.all()
 
class SousClasseViewset(ReadOnlyModelViewSet):

    serializer_class = SousClasseSerializers

    def get_queryset(self):
        return SousClasse.objects.all()
 
class NiveauxClasseViewset(ReadOnlyModelViewSet):

    serializer_class = NiveauxClasseSerializers

    def get_queryset(self):
        return NiveauxClasse.objects.all()
 
class CapaciteViewset(ReadOnlyModelViewSet):

    serializer_class = CapaciteSerializers

    def get_queryset(self):
        return Capacite.objects.all()
 
 
class EcoleMagieViewset(ReadOnlyModelViewSet):

    serializer_class = EcoleMagieSerializers

    def get_queryset(self):
        return EcoleMagie.objects.all()
 
class EtatViewset(ReadOnlyModelViewSet):

    serializer_class = EtatSerializers

    def get_queryset(self):
        return Etat.objects.all()
 
class CompetenceViewset(ReadOnlyModelViewSet):

    serializer_class = CompetenceSerializers

    def get_queryset(self):
        return Competence.objects.all()
 
class DonViewset(ReadOnlyModelViewSet):

    serializer_class = DonSerializers

    def get_queryset(self):
        return Don.objects.all()
 
class MonstreViewset(ReadOnlyModelViewSet):

    serializer_class = MonstreSerializers

    def get_queryset(self):
        return Monstre.objects.all()
 
class CapaciteMonstreViewset(ReadOnlyModelViewSet):

    serializer_class = CapaciteMonstreSerializers

    def get_queryset(self):
        return CapaciteMonstre.objects.all()
 
class RegleViewset(ReadOnlyModelViewSet):

    serializer_class = RegleSerializers

    def get_queryset(self):
        return Regle.objects.all()
 
class RegleSousSectionViewset(ReadOnlyModelViewSet):

    serializer_class = RegleSousSectionSerializers

    def get_queryset(self):
        return RegleSousSection.objects.all()
