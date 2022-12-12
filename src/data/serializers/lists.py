from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import *
from .tools import *


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

class SortListSerializers(BaseSerializers):
 
    class Meta:
        model = Sort
        fields = ['index','nom','url']

class CapaciteListSerializers(BaseSerializers):
 
    class Meta:
        model = Capacite
        fields = ['index','nom','url']

class EquipementListSerializers(BaseSerializers):
    class Meta:
        model = Equipement
        fields = ['index','nom','url']
        
    def to_representation(self, instance): 
        if isinstance(instance, Arme):
            return ArmeListSerializers(instance, context=self.context).to_representation(instance)
        elif isinstance(instance, Armure):
            return ArmureListSerializers(instance, context=self.context).to_representation(instance)
        elif isinstance(instance, EquipementAventurier):
            return EquipementAventurierListSerializers(instance, context=self.context).to_representation(instance)
        elif isinstance(instance, Sac):
            return SacListSerializers(instance, context=self.context).to_representation(instance)
        else:
            return super(EquipementListSerializers, self).to_representation(instance)
    

class CategorieEquipementListSerializers(BaseSerializers):

    class Meta:
        model = CategorieEquipement
        fields = ['index','nom','url']

class ArmeListSerializers(BaseSerializers):
    
    class Meta:
        model = Arme
        fields = ['index','nom','url']

class EquipementAventurierListSerializers(BaseSerializers):
    
    class Meta:
        model = EquipementAventurier
        fields = ['index','nom','url']

class SacListSerializers(BaseSerializers):
    
    class Meta:
        model = Sac
        fields = ['index','nom','url']
        
class ArmureListSerializers(BaseSerializers): 
    class Meta:
        model = Armure
        fields = ['index','nom','url']


class VehiculeListSerializers(BaseSerializers):
    class Meta:
        model = Vehicule
        fields = ['index','nom','url']


class ClasseListSerializers(BaseSerializers):
 
    class Meta:
        model = Classe
        fields = ['index','nom','url']

class SousClasseListSerializers(BaseSerializers):
 
    class Meta:
        model = SousClasse
        fields = ['index','nom','url']


class CompetenceListSerializers(BaseSerializers):
 
    class Meta:
        model = Competence
        fields = ['index','nom','url']


class AlignementListSerializers(ModelSerializer):
 
    class Meta:
        model = Alignement
        fields = ['index','nom','url']
        

class HistoriqueListSerializers(ModelSerializer):
    monaie_de_depart = serializers.StringRelatedField(many=True)

    class Meta:
        model = Historique
        fields = ['index','nom','url']


class InfoListSerializers(BaseSerializers):
 
    class Meta:
        model = Info
        fields = ['nom','desc']

class ProprieteArmeListSerializers(ModelSerializer):
    class Meta:
        model = ProprieteArme
        fields = ['index','nom','url']

class TypeDegatListSerializers(ModelSerializer):
 
    class Meta:
        model = TypeDegat
        fields = ['index','nom','url']


class EcoleMagieListSerializers(BaseSerializers):
 
    class Meta:
        model = EcoleMagie
        fields = ['index','nom','url']

class OptionListSerializer(BaseSerializers):
    caracteristiques = CaracteristiqueListSerializers(many=True)
    competences = CompetenceListSerializers(many=True)
    maitrises = MaitriseListSerializers(many=True)
    langues = LangueListSerializers(many=True)
    equipements = EquipementListSerializers(many=True)
    
    class Meta:
        model=Option
        fields = ['nom','desc','nombre_choix','caracteristiques','competences','maitrises','langues','equipements']



class PackEquipementClasseListSerializers(BaseSerializers):
    contenu_pack =ContenuSerializers(many=True,read_only = True)
    options = OptionListSerializer(many=True)
    class Meta:
        model=PackEquipementClasse
        fields = ['index', 'nom', 'desc', 'contenu_pack', 'options']

class NiveauListSerializers(BaseSerializers):
    class Meta:
        model = Classe
        fields = ['index','nom','url']

class NiveauxClasseListSerializers(BaseSerializers):
 
    class Meta:
        model = NiveauxClasse
        fields = ['index','nom','url']