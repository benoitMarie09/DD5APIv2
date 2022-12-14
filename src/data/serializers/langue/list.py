from data.serializers.base.base import BaseSerializers
from data.models import Langue


class LangueListSerializers(BaseSerializers):
 
    class Meta:
        model = Langue
        fields = ['index','nom','url']
