from rest_framework.serializers import ModelSerializer,StringRelatedField, Field, RelatedField
from rest_framework import serializers
from decimal import Decimal
from .models import *
from collections import OrderedDict

class PoidsField(Field):
    def to_representation(self, value):
        poids = value
        return f"{'{:f}'.format(Decimal(poids).normalize())}kg"


class BaseSerializers(ModelSerializer):
    url = serializers.SerializerMethodField()
    def get_url(self,obj):
       request = self.context.get('request')
       abs_url = obj.get_absolute_url()
       return request.build_absolute_uri(abs_url)
    def to_representation(self, instance):
        result = super(BaseSerializers, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] ])

class RaceListSerializers(BaseSerializers):
 
    class Meta:
        model = Race
        fields = ['index','nom','url']


class SousRaceListSerializers(BaseSerializers):
 
    class Meta:
        model = SousRace
        fields = ['index','nom','url']

class MaitriseListSerializers(BaseSerializers):
 
    class Meta:
        model = Maitrise
        fields = ['index','nom','url']

class LangueListSerializers(BaseSerializers):
 
    class Meta:
        model = Langue
        fields = ['index','nom','url']


class CaracteristiqueListSerializers(BaseSerializers):
 
    class Meta:
        model = Caracteristique
        fields = ['index','nom','url']

class TraitListSerializers(BaseSerializers):
 
    class Meta:
        model = Trait
        fields = ['index','nom','url']

class CompetenceSerializers(BaseSerializers):
 
    class Meta:
        model = Competence
        fields = '__all__'


class EcoleMagieSerializers(BaseSerializers):
 
    class Meta:
        model = EcoleMagie
        fields = '__all__'

class SortListSerializers(BaseSerializers):
 
    class Meta:
        model = Sort
        fields = ['index','nom','url']

class DegatSortNiveauxSerializer(BaseSerializers):
    niveau_0 = StringRelatedField(many=True)
    niveau_5 = StringRelatedField(many=True)
    niveau_11 = StringRelatedField(many=True)
    niveau_17 = StringRelatedField(many=True)
    class Meta:
        model = DegatSortNiveaux
        fields = ['desc','niveau_0','niveau_5','niveau_11','niveau_17',]

class DegatSortEmplacementsSerializer(ModelSerializer):
    emplacement_nv0 = StringRelatedField(many=True)
    emplacement_nv1 = StringRelatedField(many=True)
    emplacement_nv2 = StringRelatedField(many=True)
    emplacement_nv3 = StringRelatedField(many=True)
    emplacement_nv4 = StringRelatedField(many=True)
    emplacement_nv5 = StringRelatedField(many=True)
    emplacement_nv6 = StringRelatedField(many=True)
    emplacement_nv7 = StringRelatedField(many=True)
    emplacement_nv8 = StringRelatedField(many=True)
    emplacement_nv9 = StringRelatedField(many=True)
    class Meta:
        model = DegatSortEmplacements
        fields = ['desc','emplacement_nv0','emplacement_nv1','emplacement_nv2','emplacement_nv3','emplacement_nv4','emplacement_nv5','emplacement_nv6','emplacement_nv7','emplacement_nv8','emplacement_nv9',]

class SoinSortEmplacementsSerializer(BaseSerializers):
    emplacement_nv0 = StringRelatedField(many=True)
    emplacement_nv1 = StringRelatedField(many=True)
    emplacement_nv2 = StringRelatedField(many=True)
    emplacement_nv3 = StringRelatedField(many=True)
    emplacement_nv4 = StringRelatedField(many=True)
    emplacement_nv5 = StringRelatedField(many=True)
    emplacement_nv6 = StringRelatedField(many=True)
    emplacement_nv7 = StringRelatedField(many=True)
    emplacement_nv8 = StringRelatedField(many=True)
    emplacement_nv9 = StringRelatedField(many=True)
    class Meta:
        model = SoinSortEmplacements
        fields = ['desc','emplacement_nv0','emplacement_nv1','emplacement_nv2','emplacement_nv3','emplacement_nv4','emplacement_nv5','emplacement_nv6','emplacement_nv7','emplacement_nv8','emplacement_nv9',]

class EquipementListSerializers(BaseSerializers):

    class Meta:
        model = Equipement
        fields = ['index','nom','url']
        
    def to_representation(self, instance): 
        if isinstance(instance, Arme):
            return ArmeListSerializers(instance, context=self.context).to_representation(instance)
        elif isinstance(instance, Armure):
            return ArmureListSerializers(instance, context=self.context).to_representation(instance)
        elif isinstance(instance, Vehicule):
            return VehiculeListSerializers(instance, context=self.context).to_representation(instance)
        else:
            return super(EquipementListSerializers, self).to_representation(instance)

class PackEquipementSerializers(EquipementListSerializers):
    class Meta:
        model = PackEquipement

class CategorieEquipementListSerializers(BaseSerializers):

    class Meta:
        model = CategorieEquipement
        fields = ['index','nom','url']

class ArmeListSerializers(BaseSerializers):
    
    class Meta:
        model = Arme
        fields = ['index','nom','url']
        
class ArmureListSerializers(BaseSerializers): 
    class Meta:
        model = Armure
        fields = ['index','nom','url']


class VehiculeListSerializers(BaseSerializers):
    class Meta:
        model = Vehicule
        fields = ['index','nom','url']

class ProprieteArmeSerializers(ModelSerializer):
    class Meta:
        model = ProprieteArme
        fields = '__all__'

class TypeDegatSerializers(ModelSerializer):
 
    class Meta:
        model = TypeDegat
        fields = '__all__'


class OptionListSerializer(BaseSerializers):
    caracteristiques = CaracteristiqueListSerializers(many=True)
    competences = CompetenceSerializers(many=True)
    maitrises = MaitriseListSerializers(many=True)
    langues = LangueListSerializers(many=True)
    equipements = EquipementListSerializers(many=True)
    class Meta:
        model=Option
        fields = ['nom','desc','nombre_choix','caracteristiques','competences','maitrises','langues','equipements']
        depth = 0

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

class EtatSerializers(ModelSerializer):
 
    class Meta:
        model = Etat
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

