from data.serializers.base.base import BaseSerializers
from data.models import TypeDegat


class TypeDegatListSerializers(BaseSerializers):
 
    class Meta:
        model = TypeDegat
        fields = ['index','nom','url']
