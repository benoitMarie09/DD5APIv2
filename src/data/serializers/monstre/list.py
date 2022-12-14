from data.serializers.base.base import BaseSerializers
from data.models import Monstre, CapaciteMonstre


class MonstreSerializers(BaseSerializers):
 
    class Meta:
        model = Monstre
        fields = '__all__'
        depth = 1



class CapaciteMonstreSerializers(BaseSerializers):
 
    class Meta:
        model = CapaciteMonstre
        fields = '__all__'