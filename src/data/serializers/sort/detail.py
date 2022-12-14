from data.serializers.base.base import BaseSerializers
from data.serializers.degat.detail import DegatSortEmplacementsSerializer, DegatSortNiveauxSerializer, SoinSortEmplacementsSerializer
from data.models import EcoleMagie, Sort
from rest_framework import serializers



class SortDetailSerializers(BaseSerializers):
    composantes = serializers.StringRelatedField(many=True)
    degats_par_niveaux = DegatSortNiveauxSerializer()
    degats_par_emplacement = DegatSortEmplacementsSerializer()
    soins_par_emplacement = SoinSortEmplacementsSerializer()
    class Meta:
        model = Sort
        fields = ['index','nom','desc','ecole','niveau','composantes','composante_desc','temps_incantation','concentration','duree','portee','jets_sauvegardes','jet_attaque','soins_par_emplacement','degats_par_emplacement','degats_par_niveaux','rituel','url']


class EcoleMagieDetailSerializers(BaseSerializers):
 
    class Meta:
        model = EcoleMagie
        fields = '__all__'