from data.models import Maitrise
from data.serializers.base.base import BaseSerializers
from data.serializers.race.list import RaceListSerializers


class MaitriseDetailSerializers(BaseSerializers):
    race = RaceListSerializers(many = True)
    class Meta:
        model = Maitrise
        fields = ['index','nom','desc','type','ref_equip','ref_comp','race','url']
