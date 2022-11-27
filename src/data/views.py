from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
 
from .models import *
from .serializers import *
 
class HistoriqueViewset(ReadOnlyModelViewSet):

    serializer_class = HistoriqueSerializers

    def get_queryset(self):
        return Historique.objects.all()
 
class EquipementViewset(ReadOnlyModelViewSet):

    serializer_class = EquipementSerializers

    def get_queryset(self):
        return Equipement.objects.all()

class ArmeViewset(ReadOnlyModelViewSet):

    serializer_class = ArmeSerializers

    def get_queryset(self):
        return Arme.objects.all()

class ArmureViewset(ReadOnlyModelViewSet):

    serializer_class = ArmureSerializers

    def get_queryset(self):
        return Armure.objects.all()

class OutilViewset(ReadOnlyModelViewSet):

    serializer_class = OutilSerializers

    def get_queryset(self):
        return Outil.objects.all()

class ClasseViewset(ReadOnlyModelViewSet):

    serializer_class = ClasseSerializers

    def get_queryset(self):
        return Classe.objects.all()

class RaceViewset(ReadOnlyModelViewSet):

    serializer_class = RaceSerializers

    def get_queryset(self):
        return Race.objects.all()

class CompetenceViewset(ReadOnlyModelViewSet):

    serializer_class = CompetenceSerializers

    def get_queryset(self):
        return Competence.objects.all()
