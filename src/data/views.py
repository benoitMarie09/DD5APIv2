from rest_framework.views import APIView
from rest_framework.response import Response
 
from .models import *
from .serializers import *
 
class HistoriqueAPIView(APIView):
 
    def get(self, *args, **kwargs):
        categories = Historique.objects.all()
        serializer = HistoriqueSerializers(categories, many=True)
        return Response(serializer.data)
 
class EquipementAPIView(APIView):
 
    def get(self, *args, **kwargs):
        categories = Equipement.objects.all()
        serializer = EquipementSerializers(categories, many=True)
        return Response(serializer.data)
 
class ArmeAPIView(APIView):
 
    def get(self, *args, **kwargs):
        categories = Arme.objects.all()
        serializer = ArmeSerializers(categories, many=True)
        return Response(serializer.data)
 
class ArmureAPIView(APIView):
 
    def get(self, *args, **kwargs):
        categories = Armure.objects.all()
        serializer = ArmureSerializers(categories, many=True)
        return Response(serializer.data)
 
class OutilAPIView(APIView):
 
    def get(self, *args, **kwargs):
        categories = Outil.objects.all()
        serializer = OutilSerializers(categories, many=True)
        return Response(serializer.data)
 
class RaceAPIView(APIView):
 
    def get(self, *args, **kwargs):
        categories = Race.objects.all()
        serializer = RaceSerializers(categories, many=True)
        return Response(serializer.data)
 
class CompetenceAPIView(APIView):
 
    def get(self, *args, **kwargs):
        categories = Competence.objects.all()
        serializer = CompetenceSerializers(categories, many=True)
        return Response(serializer.data)
 
class ClasseAPIView(APIView):
 
    def get(self, *args, **kwargs):
        categories = Classe.objects.all()
        serializer = ClasseSerializers(categories, many=True)
        return Response(serializer.data)
 
