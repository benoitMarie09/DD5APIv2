from rest_framework.serializers import ModelSerializer, Field, RelatedField, StringRelatedField
from rest_framework import serializers
from decimal import Decimal
from ..models import *
from collections import OrderedDict


class SortsClasseField(serializers.SerializerMethodField):
    def get_url(self,obj):
       request = self.context.get('request')
       abs_url = obj.get_absolute_url()
       return request.build_absolute_uri(abs_url)
    def to_representation(self, value):
        
        return f"{value}"

class PoidsField(Field):

    def to_representation(self, value):
        poids = value
        return f"{'{:f}'.format(Decimal(poids).normalize())}kg"

class ContenuSerializers(RelatedField):
    def get_url(self,obj):
       request = self.context.get('request')
       abs_url = obj.get_absolute_url()
       return request.build_absolute_uri(abs_url)
    def to_representation(self,value):
        return {'equipement':value.equipement.nom,'quantite':value.quantite, 'url': self.get_url(value.equipement) }

class EmplacementSortField(RelatedField):
    def to_representation(self, value):
        return {'Sorts mineurs connus':value.nv_0, 'Sorts connus':value.sort_connu,'Emplacements de sorts':{
            'niveau 1':value.nv_1,
            'niveau 2':value.nv_2,
            'niveau 3':value.nv_3,
            'niveau 4':value.nv_4,
            'niveau 5':value.nv_5,
            'niveau 6':value.nv_6,
            'niveau 7':value.nv_7,
            'niveau 8':value.nv_8,
            'niveau 9':value.nv_9,
        }}

class SpecifiqueField(RelatedField):
    def to_representation(self, value):
        return {value.specifique.nom : value.quantite}


class BaseSerializers(ModelSerializer):
    url = serializers.SerializerMethodField()
    def get_url(self,obj):
       request = self.context.get('request')
       abs_url = obj.get_absolute_url()
       return request.build_absolute_uri(abs_url)
    def to_representation(self, instance):
        result = super(BaseSerializers, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] ])


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


class SousClasseSerializers(ModelSerializer):
 
    class Meta:
        model = SousClasse
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

