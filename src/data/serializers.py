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

class MaitriseDetailSerializers(BaseSerializers):
    race = RaceListSerializers(many = True)
    class Meta:
        model = Maitrise
        fields = ['index','nom','desc','type','ref_equip','ref_comp','race','url']

class OptionsMaitriseSerializer(ModelSerializer):
    parmis = MaitriseListSerializers(many=True)
    class Meta:
        model=OptionsMaitrise
        fields = ['nom','desc','nombre_choix','parmis']

class LangueListSerializers(BaseSerializers):
 
    class Meta:
        model = Langue
        fields = ['index','nom','url']

class LangueDetailSerializers(BaseSerializers):
 
    class Meta:
        model = Langue
        fields = ['index','nom','type','desc','race_typiques','url']

class OptionsLangueSerializer(ModelSerializer):
    parmis = LangueListSerializers(many=True)
    class Meta:
        model=OptionsLangue
        fields = ['nom','desc','nombre_choix','parmis']


class CaracteristiqueListSerializers(BaseSerializers):
 
    class Meta:
        model = Caracteristique
        fields = ['index','nom','url']

class CaracteristiqueDetailSerializers(BaseSerializers):
 
    class Meta:
        model = Caracteristique
        fields = ['index','nom','desc','url']

class OptionsCaracteristiqueSerializer(ModelSerializer):
    parmis = CaracteristiqueListSerializers(many=True)
    class Meta:
        model=OptionsCaracteristique
        fields = ['nom','desc','nombre_choix','parmis']

class TraitListSerializers(BaseSerializers):
 
    class Meta:
        model = Trait
        fields = ['index','nom','url']

class TraitDetailSerializers(BaseSerializers):
    race = RaceListSerializers(many = True)
    class Meta:
        model = Trait
        fields = ['index','nom','desc','race','url']

class CompetenceSerializers(ModelSerializer):
 
    class Meta:
        model = Competence
        fields = '__all__'


class EcoleMagieSerializers(ModelSerializer):
 
    class Meta:
        model = EcoleMagie
        fields = '__all__'

class SortListSerializers(BaseSerializers):
 
    class Meta:
        model = Sort
        fields = ['index','nom','url']

class SortDetailSerializers(BaseSerializers):
    composantes = StringRelatedField(many=True)
    temps_incantation = StringRelatedField()
    duree = StringRelatedField()
    portee = StringRelatedField()
    cible = StringRelatedField()
    degats = StringRelatedField(many=True)
    class Meta:
        model = Sort
        fields = ['index','nom','desc','ecole','niveau','composantes','composante_desc','temps_incantation','concentration','duree','portee','cible','degats','jets_sauvegardes','jet_attaque','rituel','url']

class OptionsSortSerializer(ModelSerializer):
    parmis = SortListSerializers(many=True)
    class Meta:
        model=OptionsSort
        fields = ['nom','desc','nombre_choix','parmis']


class SousRaceDetailSerializers(BaseSerializers):
    race = RaceListSerializers()
    caracteristique = StringRelatedField(many=True)
    maitrises_depart = MaitriseListSerializers(many=True)
    maitrises_option = OptionsMaitriseSerializer()
    langues = LangueListSerializers(many=True)
    langues_option = OptionsLangueSerializer()
    taille = StringRelatedField()
    traits = TraitListSerializers(many=True)
    sorts = SortListSerializers(many=True)
    sorts_option = OptionsSortSerializer()
    class Meta:
        model = Race
        fields = ['index','nom','race','vitesse','caracteristique','bonus_caracteristique_option','age','poids','taille','taille_details','maitrises_depart','maitrises_option','langues','langues_option','langues_desc','traits','sorts','sorts_option','url',]
        depth = 2
   

class RaceDetailSerializers(BaseSerializers):
    sous_race = SousRaceListSerializers(many=True)
    caracteristique = StringRelatedField(many=True)
    maitrises_depart = MaitriseListSerializers(many=True)
    langues = LangueListSerializers(many=True)
    taille = StringRelatedField()
    traits = TraitListSerializers(many=True)
    class Meta:
        model = Race
        fields = ['index','nom','vitesse','caracteristique','bonus_caracteristique_option','age','poids','taille','taille_details','maitrises_depart','maitrises_option','langues','langues_option','langues_desc','traits','sorts','sorts_option','sous_race','url',]
        depth = 2

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
        fields = ['index','nom','url']
    
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
        fields = ['index','nom','url']

class ArmureDetailSerializers(BaseSerializers):
    prix = serializers.StringRelatedField(many=True)
    poids = PoidsField()
    CA = serializers.StringRelatedField()
    class Meta:
        model = Armure
        fields = ['index','nom','categorie_armure','prix','CA','poids','force_min','desaventage_discretion','url']

class VehiculeListSerializers(BaseSerializers):
    class Meta:
        model = Vehicule
        fields = ['index','nom','url']
#['index','nom','categorie','prix','capacité','vitesse','poids','desc','capacite','url']
class VehiculeDetailSerializers(BaseSerializers):
    prix = serializers.StringRelatedField(many=True)
    poids = PoidsField()
    class Meta:
        model = Vehicule
        fields = ['index','nom','categorie','prix','capacite','vitesse','poids','desc','url']

class ProprieteArmeSerializers(ModelSerializer):
    class Meta:
        model = ProprieteArme
        fields = '__all__'

class TypeDegatSerializers(ModelSerializer):
 
    class Meta:
        model = TypeDegat
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

