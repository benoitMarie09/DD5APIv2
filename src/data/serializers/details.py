from rest_framework.serializers import ModelSerializer,StringRelatedField
from rest_framework import serializers
from ..models import *
from .lists import *



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
        elif isinstance(instance, EquipementAventurier):
            return EquipementAventurierDetailSerializers(instance, context=self.context).to_representation(instance)
        elif isinstance(instance, Sac):
            return SacDetailSerializers(instance, context=self.context).to_representation(instance)
        else:
            return super(EquipementDetailSerializers, self).to_representation(instance)

class EquipementAventurierDetailSerializers(BaseSerializers):
    prix = serializers.StringRelatedField(many=True)
    poids = PoidsField()
    class Meta:
        model = EquipementAventurier
        fields= ['index','nom','categorie_equipement','categorie_equipement_aventurier','prix','poids','desc','url']


class SacDetailSerializers(BaseSerializers):
    prix = serializers.StringRelatedField(many=True)
    contenu = EquipementAventurierListSerializers(many=True)
    class Meta:
        model = Sac
        fields= ['index','nom','categorie_equipement','prix','contenu','desc','url']
    
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

class OptionPackDetailSerializer(OptionListSerializer):
    packs_equipements = PackEquipementClasseListSerializers(many=True)
    class Meta:
        model=Option
        fields = ['desc','nombre_choix','packs_equipements']


class IncantationDetailSerializers(BaseSerializers):
    info = InfoListSerializers(many=True)
    caracteristique = CaracteristiqueListSerializers()
    class Meta:
        model = Incantation
        fields = ['nom','caracteristique','info']


class NiveauDetailSerializers(BaseSerializers):
    capacite = CapaciteListSerializers(many=True)
    emplacements_sorts = EmplacementSortField(read_only = True)
    specifique = SpecifiqueField(many=True, read_only = True)

    class Meta:
        model = Niveau
        fields = ['index', 'nom','niveau','bonus_maitrise','capacite','emplacements_sorts','specifique','url']



class ClasseDetailSerializers(BaseSerializers):
    maitrises = MaitriseListSerializers(many=True)
    options_maitrises = OptionListSerializer()
    options_competences = OptionListSerializer()
    equipements_depart = EquipementListSerializers(many=True)
    equipements_options = OptionPackDetailSerializer()
    incantation = IncantationDetailSerializers()
    sorts = serializers.SerializerMethodField()
    niveaux = serializers.SerializerMethodField()
    class Meta:
        model = Classe
        fields = ['index','nom','pv','jets_sauvegardes','maitrises','options_maitrises','options_competences','equipements_depart','equipements_options','incantation', 'sorts', 'niveaux']
        depth = 3
    def get_attribute(self, instance):
        return instance
    def get_sorts(self,obj):
       request = self.context.get('request')
       abs_url = obj.get_absolute_url()
       sorts_url = request.build_absolute_uri(abs_url+'sorts')
       return sorts_url
    def get_niveaux(self,obj):
       request = self.context.get('request')
       abs_url = obj.get_absolute_url()
       niveaux_url = request.build_absolute_uri(abs_url+'niveaux')
       return niveaux_url


class NiveauxClasseDetailSerializers(BaseSerializers):
    niveaux = NiveauDetailSerializers(many=True)
    class Meta:
        model = NiveauxClasse
        fields = ['classe','niveaux','url']


class CapaciteDetailSerializers(BaseSerializers):
    class Meta:
        model = Capacite
        fields = ['index','nom','classe','sous_classe','desc']

class AlignementDetailSerializers(ModelSerializer):
 
    class Meta:
        model = Alignement
        fields = '__all__'

class HistoriqueDetailSerializers(BaseSerializers):
    maitrises_depart = MaitriseListSerializers(many=True)
    langues_options = OptionListSerializer()
    maitrises_options =OptionListSerializer()
    equipements_options =OptionListSerializer()
    competences = CompetenceListSerializers(many=True)
    equipements_depart = EquipementListSerializers(many=True)
    monaie_de_depart = StringRelatedField(many=True)
    class Meta:
        model = Historique
        fields = ['index','nom','desc','maitrises_depart','maitrises_options','competences','langues_options','equipements_depart','equipements_options','monaie_de_depart','url']
        depth = 1

class EtatDetailSerializers(BaseSerializers):

    class Meta:
        model = Etat
        fields = ['index','nom','desc','url']

class ProprieteArmeDetailSerializers(BaseSerializers):
    class Meta:
        model = ProprieteArme
        fields = ['index','nom','desc','url']

class TypeDegatDetailSerializers(BaseSerializers):
 
    class Meta:
        model = TypeDegat
        fields = ['index','nom','desc','url']

class CompetenceDetailSerializers(BaseSerializers):
 
    class Meta:
        model = Competence
        fields = '__all__'


class EcoleMagieDetailSerializers(BaseSerializers):
 
    class Meta:
        model = EcoleMagie
        fields = '__all__'