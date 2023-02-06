from data.serializers.base.base import BaseSerializers
from data.models import PJ


class PJListSerializers(BaseSerializers):
 
    class Meta:
        model = PJ
        fields = ['index','nom','url']