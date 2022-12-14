from data.serializers.base.base import BaseSerializers
from data.models import Caracteristique


class CaracteristiqueDetailSerializers(BaseSerializers):
 
    class Meta:
        model = Caracteristique
        fields = ['index','nom','desc','url']