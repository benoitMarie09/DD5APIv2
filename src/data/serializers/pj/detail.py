from rest_framework import serializers
from data.models import PJ, Race
from data.serializers.base.base import BaseSerializers
from data.serializers.race.list import RaceListSerializers
from data.serializers.caracteristique.list import CaracteristiqueListSerializers

class PJDetailSerializers(BaseSerializers):
    
    race = RaceListSerializers()

    class Meta:
        model = PJ
        fields = ["index","nom","desc","race",]
        depth = 2
    
    def create(self, validated_data):
        id_param = validated_data.pop('race')
        my_race = Race.objects.get(index=id_param)
        pj = PJ.objects.create(race=my_race.index)
        return pj