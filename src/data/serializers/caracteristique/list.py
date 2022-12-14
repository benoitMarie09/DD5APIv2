from data.serializers.base.base import BaseSerializers
from data.models import Caracteristique


class CaracteristiqueListSerializers(BaseSerializers):
 
    class Meta:
        model = Caracteristique
        fields = ['index','nom','url']