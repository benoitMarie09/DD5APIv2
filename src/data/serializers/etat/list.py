from data.serializers.base.base import BaseSerializers
from data.models import Etat


class EtatListSerializers(BaseSerializers):
 
    class Meta:
        model = Etat
        fields = ['index','nom','url']
