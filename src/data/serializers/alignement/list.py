from data.serializers.base.base import BaseSerializers
from data.models import Alignement


class AlignementListSerializers(BaseSerializers):
 
    class Meta:
        model = Alignement
        fields = ['index','nom','url']
        