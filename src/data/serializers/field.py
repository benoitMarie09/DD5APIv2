from rest_framework.serializers import  Field, RelatedField
from rest_framework import serializers
from decimal import Decimal



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

class ContenuField(RelatedField):
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

