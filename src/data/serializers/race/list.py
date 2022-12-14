from data.serializers.base.base import BaseSerializers
from data.serializers.maitrise.list import MaitriseListSerializers
from data.serializers.option.list import OptionListSerializer
from data.models import Race, SousRace, Trait


class RaceMaitrisesOptionsList(BaseSerializers):
    maitrises_depart = MaitriseListSerializers(many=True)
    maitrises_option = OptionListSerializer()
    class Meta:
        model = Race
        fields = ['maitrises_depart','maitrises_option']


class RaceListSerializers(BaseSerializers):
 
    class Meta:
        model = Race
        fields = ['index','nom','url']


class SousRaceListSerializers(BaseSerializers):
 
    class Meta:
        model = SousRace
        fields = ['index','nom','url']


class TraitListSerializers(BaseSerializers):
 
    class Meta:
        model = Trait
        fields = ['index','nom','url']
