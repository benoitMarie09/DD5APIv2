from rest_framework import serializers
from data.serializers.base.base import BaseSerializers
from data.serializers.equipement.list import EquipementListSerializers
from data.serializers.maitrise.list import MaitriseListSerializers
from data.serializers.option.list import OptionListSerializer
from data.serializers.race.detail import IncantationDetailSerializers, OptionPackDetailSerializer
from data.models import Classe, SousClasse, Capacite, NiveauxClasse


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



class CapaciteDetailSerializers(BaseSerializers):
    class Meta:
        model = Capacite
        fields = ['index','nom','classe','sous_classe','desc']


class SousClasseSerializers(BaseSerializers):
 
    class Meta:
        model = SousClasse
        fields = '__all__'


