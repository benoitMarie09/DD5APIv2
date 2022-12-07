from rest_framework.serializers import ModelSerializer, Field
from rest_framework import serializers
from decimal import Decimal
from .models import *

class PoidsField(Field):
    def to_representation(self, value):
        poids = value
        return f"{Decimal(poids).normalize()}kg"

class BaseSerializers(ModelSerializer):
    url = serializers.SerializerMethodField()
    def get_url(self,obj):
       request = self.context.get('request')
       abs_url = obj.get_absolute_url()
       return request.build_absolute_uri(abs_url)

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
    monaie_de_depart = serializers.StringRelatedField(many=True)

    class Meta:
        model = Historique
        fields = '__all__'
        depth = 1


class EquipementListSerializers(BaseSerializers):
    prix = serializers.StringRelatedField(many=True)

    class Meta:
        model = Equipement
        fields = ['index','nom','categorie_equipement','prix','url']
        
    def to_representation(self, instance): 
        if isinstance(instance, Arme):
            return ArmeListSerializers(instance, context=self.context).to_representation(instance)
        elif isinstance(instance, Armure):
            return ArmureListSerializers(instance, context=self.context).to_representation(instance)
        elif isinstance(instance, Vehicule):
            return VehiculeListSerializers(instance, context=self.context).to_representation(instance)
        else:
            return super(EquipementListSerializers, self).to_representation(instance)

class EquipementDetailSerializers(BaseSerializers):
    prix = serializers.StringRelatedField(many=True)
    poids = PoidsField()
    class Meta:
        model = Equipement
        fields= ['index','nom','categorie_equipement','prix','poids','desc','url']
    def to_representation(self, instance): 
        if isinstance(instance, Arme):
            return ArmeDetailSerializers(instance, context=self.context).to_representation(instance)
        elif isinstance(instance, Armure):
            return ArmureDetailSerializers(instance, context=self.context).to_representation(instance)
        elif isinstance(instance, Vehicule):
            return VehiculeDetailSerializers(instance, context=self.context).to_representation(instance)
        else:
            return super(EquipementDetailSerializers, self).to_representation(instance)


class PackEquipementSerializers(EquipementListSerializers):
    class Meta:
        model = PackEquipement

class CategorieEquipementListSerializers(BaseSerializers):

    class Meta:
        model = CategorieEquipement
        fields = ['index','nom','url']

class CategorieEquipementDetailSerializers(BaseSerializers):
    equipement_set = EquipementListSerializers(many=True,read_only=True)
    class Meta:
        model = CategorieEquipement
        fields = ['index','nom','desc','equipement_set','url']

class ArmeListSerializers(BaseSerializers):
    
    class Meta:
        model = Arme
        fields = ['index','nom','type','prix','url']
    
class ArmeDetailSerializers(BaseSerializers):
    prix = serializers.StringRelatedField(many=True)
    poids = PoidsField()
    degat_une_main = serializers.StringRelatedField()
    degat_deux_mains = serializers.StringRelatedField()
    degat_distance = serializers.StringRelatedField()
    portee = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Arme
        fields = ['index','nom','categorie_equipement','categorie_arme','type_portee','type','prix','poids','degat_une_main','degat_deux_mains','degat_distance','portee','propriete','special','url']

class ArmureListSerializers(BaseSerializers):
    
    class Meta:
        model = Armure
        fields = ['index','nom','categorie_armure','prix','url']

class ArmureDetailSerializers(BaseSerializers):
    CA = serializers.StringRelatedField()
    class Meta:
        model = Armure
        fields = ['index','nom','categorie_armure','prix','CA','poids','force_min','desaventage_discretion','url']

class VehiculeListSerializers(EquipementListSerializers):
    class Meta:
        model = Vehicule
        fields = ['index','nom','url']

class VehiculeDetailSerializers(EquipementListSerializers):
    class Meta:
        model = Vehicule
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

