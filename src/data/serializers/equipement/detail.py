from data import serializers
from data.models import Equipement, EquipementAventurier, Sac, Arme, Armure, Vehicule, CategorieEquipement, ProprieteArme
from data.serializers.base.base import BaseSerializers
from data.serializers.equipement.list import ArmeListSerializers, ArmureListSerializers, EquipementAventurierListSerializers, EquipementListSerializers
from data.serializers.field import PoidsField

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
        fields = ['index','nom','categorie_equipement','categorie_arme','portee','prix','poids','degat_une_main','degat_deux_mains','degat_distance','portee','propriete','special','url']


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


class ProprieteArmeDetailSerializers(BaseSerializers):
    class Meta:
        model = ProprieteArme
        fields = ['index','nom','desc','url']