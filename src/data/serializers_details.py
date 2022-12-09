from rest_framework.serializers import ModelSerializer,StringRelatedField, Field, RelatedField
from rest_framework import serializers
from decimal import Decimal
from .models import *
from collections import OrderedDict
from .serializers_lists import *



class MaitriseDetailSerializers(BaseSerializers):
    race = RaceListSerializers(many = True)
    class Meta:
        model = Maitrise
        fields = ['index','nom','desc','type','ref_equip','ref_comp','race','url']


class LangueDetailSerializers(BaseSerializers):
 
    class Meta:
        model = Langue
        fields = ['index','nom','type','desc','race_typiques','url']


class CaracteristiqueDetailSerializers(BaseSerializers):
 
    class Meta:
        model = Caracteristique
        fields = ['index','nom','desc','url']


class TraitDetailSerializers(BaseSerializers):
    race = RaceListSerializers(many = True)
    class Meta:
        model = Trait
        fields = ['index','nom','desc','race','url']


class SortDetailSerializers(BaseSerializers):
    composantes = StringRelatedField(many=True)
    degats_par_niveaux = DegatSortNiveauxSerializer()
    degats_par_emplacement = DegatSortEmplacementsSerializer()
    soins_par_emplacement = SoinSortEmplacementsSerializer()
    class Meta:
        model = Sort
        fields = ['index','nom','desc','ecole','niveau','composantes','composante_desc','temps_incantation','concentration','duree','portee','jets_sauvegardes','jet_attaque','soins_par_emplacement','degats_par_emplacement','degats_par_niveaux','rituel','url']



class SousRaceDetailSerializers(BaseSerializers):
    race = RaceListSerializers()
    caracteristique = StringRelatedField(many=True)
    maitrises_depart = MaitriseListSerializers(many=True)
    maitrises_option = OptionListSerializer()
    langues = LangueListSerializers(many=True)
    langues_option = OptionListSerializer()
    taille = StringRelatedField()
    traits = TraitListSerializers(many=True)
    sorts = SortListSerializers(many=True)
    sorts_option = OptionListSerializer()
    class Meta:
        model = Race
        fields = ['index','nom','race','vitesse','caracteristique','bonus_caracteristique_option','age','poids','taille','taille_details','maitrises_depart','maitrises_option','langues','langues_option','langues_desc','traits','sorts','sorts_option','url',]
        depth = 2
   

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


class ArmureDetailSerializers(BaseSerializers):
    prix = serializers.StringRelatedField(many=True)
    poids = PoidsField()
    CA = serializers.StringRelatedField()
    class Meta:
        model = Armure
        fields = ['index','nom','categorie_armure','prix','CA','poids','force_min','desaventage_discretion','url']


class VehiculeDetailSerializers(BaseSerializers):
    prix = serializers.StringRelatedField(many=True)
    poids = PoidsField()
    class Meta:
        model = Vehicule
        fields = ['index','nom','categorie','prix','capacite','vitesse','poids','desc','url']

        
class CategorieEquipementDetailSerializers(BaseSerializers):
    equipement_set = EquipementListSerializers(many=True,read_only=True)
    categorie_arme = ArmeListSerializers(many=True,read_only=True)
    categorie_armure = ArmureListSerializers(many=True,read_only=True)
    categorie_arme_portee = ArmeListSerializers(many=True,read_only=True)
    categorie_portee = ArmeListSerializers(many=True,read_only=True)
    class Meta:
        model = CategorieEquipement
        fields = ['index','nom','desc','equipement_set','categorie_arme','categorie_armure','categorie_arme_portee','categorie_portee','url']

class RaceDetailSerializers(BaseSerializers):
    sous_race = SousRaceListSerializers(many=True)
    caracteristique = StringRelatedField(many=True)
    maitrises_depart = MaitriseListSerializers(many=True)
    langues = LangueListSerializers(many=True)
    taille = StringRelatedField()
    traits = TraitListSerializers(many=True)
    maitrises_option = OptionListSerializer()
    langues_option = OptionListSerializer()
    sorts_option = OptionListSerializer()
    bonus_caracteristique_option = OptionListSerializer()
    class Meta:
        model = Race
        fields = ['index','nom','vitesse','caracteristique','bonus_caracteristique_option','age','poids','taille','taille_details','maitrises_depart','maitrises_option','langues','langues_option','langues_desc','traits','sorts','sorts_option','sous_race','url',]
        depth = 2
