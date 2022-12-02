from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
 
from .models import *
from .serializers import *
 
class RaceViewset(ReadOnlyModelViewSet):

    serializer_class = RaceSerializers

    def get_queryset(self):
        return Race.objects.all()
 
class MaitriseViewset(ReadOnlyModelViewSet):

    serializer_class = MaitriseSerializers

    def get_queryset(self):
        return Maitrise.objects.all()
 
class LangueViewset(ReadOnlyModelViewSet):

    serializer_class = LangueSerializers

    def get_queryset(self):
        return Langue.objects.all()
 
class SousRaceViewset(ReadOnlyModelViewSet):

    serializer_class = SousRaceSerializers

    def get_queryset(self):
        return SousRace.objects.all()
 
class CaracteristiqueViewset(ReadOnlyModelViewSet):

    serializer_class = CaracteristiqueSerializers

    def get_queryset(self):
        return Caracteristique.objects.all()
 
class TraitViewset(ReadOnlyModelViewSet):

    serializer_class = TraitSerializers

    def get_queryset(self):
        return Trait.objects.all()
 
class AlignementViewset(ReadOnlyModelViewSet):

    serializer_class = AlignementSerializers

    def get_queryset(self):
        return Alignement.objects.all()
 
class HistoriqueViewset(ReadOnlyModelViewSet):

    serializer_class = HistoriqueSerializers

    def get_queryset(self):
        return Historique.objects.all()
 
class EquipementViewset(ReadOnlyModelViewSet):

    serializer_class = EquipementSerializers

    def get_queryset(self):
        return Equipement.objects.all()
 
class CategorieEquipementViewset(ReadOnlyModelViewSet):

    serializer_class = CategorieEquipementSerializers

    def get_queryset(self):
        return CategorieEquipement.objects.all()
 
class ArmeViewset(ReadOnlyModelViewSet):

    serializer_class = ArmeSerializers

    def get_queryset(self):
        return Arme.objects.all()
 
class ArmureViewset(ReadOnlyModelViewSet):

    serializer_class = ArmureSerializers

    def get_queryset(self):
        return Armure.objects.all()
 
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
 
class SortViewset(ReadOnlyModelViewSet):

    serializer_class = SortSerializers

    def get_queryset(self):
        return Sort.objects.all()
 
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
