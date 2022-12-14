from data.serializers.base.base import BaseSerializers
from data.models import EcoleMagie, Sort


class EcoleMagieListSerializers(BaseSerializers):
 
    class Meta:
        model = EcoleMagie
        fields = ['index','nom','url']

class SortListSerializers(BaseSerializers):
 
    class Meta:
        model = Sort
        fields = ['index','nom','url']
