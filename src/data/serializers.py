from rest_framework.serializers import ModelSerializer
 
from .models import *


class RaceSerializers(ModelSerializer):
 
    class Meta:
        model = Race
        fields = '__all__'

class MaitriseSerializers(ModelSerializer):
 
    class Meta:
        model = Maitrise
        fields = '__all__'

class LangueSerializers(ModelSerializer):
 
    class Meta:
        model = Langue
        fields = '__all__'

class SousRaceSerializers(ModelSerializer):
 
    class Meta:
        model = SousRace
        fields = '__all__'

class CaracteristiqueSerializers(ModelSerializer):
 
    class Meta:
        model = Caracteristique
        fields = '__all__'

class TraitSerializers(ModelSerializer):
 
    class Meta:
        model = Trait
        fields = '__all__'

class AlignementSerializers(ModelSerializer):
 
    class Meta:
        model = Alignement
        fields = '__all__'

class HistoriqueSerializers(ModelSerializer):
 
    class Meta:
        model = Historique
        fields = '__all__'

class EquipementSerializers(ModelSerializer):
 
    class Meta:
        model = Equipement
        fields = '__all__'

class CategorieEquipementSerializers(ModelSerializer):
 
    class Meta:
        model = CategorieEquipement
        fields = '__all__'

class ArmeSerializers(ModelSerializer):
 
    class Meta:
        model = Arme
        fields = '__all__'

class ArmureSerializers(ModelSerializer):
 
    class Meta:
        model = Armure
        fields = '__all__'

class ProprieteArmeSerializers(ModelSerializer):
 
    class Meta:
        model = ProprieteArme
        fields = '__all__'

class TypeDegatSerializers(ModelSerializer):
 
    class Meta:
        model = TypeDegat
        fields = '__all__'

class ClasseSerializers(ModelSerializer):
 
    class Meta:
        model = Classe
        fields = '__all__'

class IncantationSerializers(ModelSerializer):
 
    class Meta:
        model = Incantation
        fields = '__all__'

class SousClasseSerializers(ModelSerializer):
 
    class Meta:
        model = SousClasse
        fields = '__all__'

class NiveauxClasseSerializers(ModelSerializer):
 
    class Meta:
        model = NiveauxClasse
        fields = '__all__'
        depth = 2

class CapaciteSerializers(ModelSerializer):
 
    class Meta:
        model = Capacite
        fields = '__all__'

class SortSerializers(ModelSerializer):
 
    class Meta:
        model = Sort
        fields = '__all__'

class EcoleMagieSerializers(ModelSerializer):
 
    class Meta:
        model = EcoleMagie
        fields = '__all__'

class EtatSerializers(ModelSerializer):
 
    class Meta:
        model = Etat
        fields = '__all__'

class CompetenceSerializers(ModelSerializer):
 
    class Meta:
        model = Competence
        fields = '__all__'

class DonSerializers(ModelSerializer):
 
    class Meta:
        model = Don
        fields = '__all__'

class MonstreSerializers(ModelSerializer):
 
    class Meta:
        model = Monstre
        fields = '__all__'
        depth = 1

class CapaciteMonstreSerializers(ModelSerializer):
 
    class Meta:
        model = CapaciteMonstre
        fields = '__all__'

class RegleSerializers(ModelSerializer):
 
    class Meta:
        model = Regle
        fields = '__all__'

class RegleSousSectionSerializers(ModelSerializer):
 
    class Meta:
        model = RegleSousSection
        fields = '__all__'

