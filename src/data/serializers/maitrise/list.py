from data.serializers.base.base import BaseSerializers
from data.models import Maitrise


class MaitriseListSerializers(BaseSerializers):
 
    class Meta:
        model = Maitrise
        fields = ['index','nom','url']

