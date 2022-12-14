from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
 
from data.models import Classe, Capacite, SousClasse
from data.serializers import CapaciteListSerializers, CapaciteDetailSerializers, SousClasseSerializers, IncantationDetailSerializers, SortListSerializers, CapaciteListSerializers, MaitriseListSerializers, ClasseListSerializers, ClasseDetailSerializers, NiveauDetailSerializers

 
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


 
class SousClasseViewset(ReadOnlyModelViewSet):

    serializer_class = SousClasseSerializers

    def get_queryset(self):
        return SousClasse.objects.all()
 
 
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
 
 