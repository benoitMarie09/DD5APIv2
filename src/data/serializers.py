from rest_framework.serializers import ModelSerializer
 
from .models import *
 
class HistoriqueSerializers(ModelSerializer):
 
    class Meta:
        model = Historique
        fields = '__all__'

class EquipementSerializers(ModelSerializer):
 
    class Meta:
        model = Equipement
        fields = '__all__'

class ArmeSerializers(ModelSerializer):
 
    class Meta:
        model = Arme
        fields = '__all__'

class ArmureSerializers(ModelSerializer):
 
    class Meta:
        model = Armure
        fields = '__all__'

class OutilSerializers(ModelSerializer):
 
    class Meta:
        model = Outil
        fields = '__all__'

class RaceSerializers(ModelSerializer):
 
    class Meta:
        model = Race
        fields = '__all__'

class CompetenceSerializers(ModelSerializer):
 
    class Meta:
        model = Competence
        fields = '__all__'

class ClasseSerializers(ModelSerializer):
 
    class Meta:
        model = Classe
        fields = '__all__'