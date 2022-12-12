from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
 
from .models import *
from .serializers.details import *
from .serializers.lists import *
 

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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = Alignement
    serializer_classes = {
        'list':AlignementListSerializers,
        'retrieve':AlignementDetailSerializers,
    }

    default_serializer_class = AlignementListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return Alignement.objects.all()
 
class HistoriqueViewset(ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = Historique
    serializer_classes = {
        'list':HistoriqueListSerializers,
        'retrieve':HistoriqueDetailSerializers,
    }

    default_serializer_class = HistoriqueListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return Historique.objects.all()
 
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
 
class ClasseViewset(ReadOnlyModelViewSet):

    model = Classe
    serializer_classes = {
        'list':ClasseListSerializers,
        'retrieve':ClasseDetailSerializers,
    }

    default_serializer_class = ClasseListSerializers

    @action(detail=True,url_path='sous-classes')
    def sous_classes(self, request, pk=None):
        classe = self.get_object()
        sous_classes = classe.sous_classe.all()
        serializers = SousClasseSerializers(sous_classes,context = {'request':request}, many=True)
        return Response(serializers.data)

    @action(detail=True,url_path='incantation')
    def incantation(self, request, pk=None):
        classe = self.get_object()
        incantation = classe.incantation
        serializers = IncantationDetailSerializers(incantation,context = {'request':request})
        return Response(serializers.data)

    # @action(detail=True,url_path='multiclasse')
    # def sous_classes(self, request, pk=None):
    #     classe = self.get_object()
    #     sous_classes = classe.sous_classe.all()
    #     serializers = SousClasseSerializers(sous_classes, many=True)
    #     return Response(serializers.data)

    @action(detail=True,url_path='sorts')
    def sorts(self, request, pk=None):
        classe = self.get_object()
        sorts = classe.sorts.all()
        serializers = SortListSerializers(sorts,context = {'request':request}, many=True)
        return Response(serializers.data)

    @action(detail=True,url_path='capacites')
    def capacites(self, request, pk=None):
        classe = self.get_object()
        capacites = classe.capacite.all()
        serializers = CapaciteListSerializers(capacites,context = {'request':request}, many=True)
        return Response(serializers.data)

    @action(detail=True,url_path='maitrises')
    def maitrises(self, request,pk=None):
        classe = self.get_object()
        maitrises = classe.maitrises.all()
        serializers = MaitriseListSerializers(maitrises,context = {'request':request}, many=True)
        return Response(serializers.data)

    @action(detail=True,url_path='niveaux/(?P<niveau>\w+)/capacite', url_name='niveau_capacite')
    def niveau_capacite(self, request,pk,niveau):
        capacite = self.get_object().niveaux.get(niveau=niveau).capacite.all()
        print(capacite)
        serializers = CapaciteListSerializers(capacite,context = {'request':request},many=True)
        return Response(serializers.data)

    @action(detail=True,url_path='niveaux/(?P<niveau>\w+)', url_name='niveau')
    def niveaux_detail(self, request,pk,niveau):
        niv = self.get_object().niveaux.get(niveau=niveau)
        serializers = NiveauDetailSerializers(niv,context = {'request':request})
        return Response(serializers.data)

    @action(detail=True,url_path='niveaux', url_name='niveaux')
    def niveaux(self, request,pk=None):
        classe = self.get_object()
        niveaux = classe.niveaux.all()
        serializers = NiveauDetailSerializers(niveaux,context = {'request':request}, many=True)
        return Response(serializers.data)


    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return Classe.objects.all()

 
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
 
class TypeDegatViewset(ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = TypeDegat
    serializer_classes = {
        'list':TypeDegatListSerializers,
        'retrieve':TypeDegatDetailSerializers,
    }

    default_serializer_class = TypeDegatListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return TypeDegat.objects.all()
 
 
class SousClasseViewset(ReadOnlyModelViewSet):

    serializer_class = SousClasseSerializers

    def get_queryset(self):
        return SousClasse.objects.all()
 
class NiveauxClasseViewset(ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = NiveauxClasse
    serializer_classes = {
        'list':NiveauxClasseListSerializers,
        'retrieve':NiveauxClasseDetailSerializers,
    }

    default_serializer_class = NiveauxClasseListSerializers


    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return NiveauxClasse.objects.all()
 
class CapaciteViewset(ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = Capacite
    serializer_classes = {
        'list':CapaciteListSerializers,
        'retrieve':CapaciteDetailSerializers,
    }

    default_serializer_class = CapaciteListSerializers


    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return Capacite.objects.all()
 
 
class EcoleMagieViewset(ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = EcoleMagie
    serializer_classes = {
        'list':EcoleMagieListSerializers,
        'retrieve':EcoleMagieDetailSerializers,
    }

    default_serializer_class = SortListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return EcoleMagie.objects.all()
 
class EtatViewset(ReadOnlyModelViewSet):

    serializer_class = EtatSerializers

    def get_queryset(self):
        return Etat.objects.all()
 
class CompetenceViewset(ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = Competence
    serializer_classes = {
        'list':CompetenceListSerializers,
        'retrieve':CompetenceDetailSerializers,
    }

    default_serializer_class = CompetenceListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

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
