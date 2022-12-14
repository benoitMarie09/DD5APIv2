from data.models import Etat
from data.serializers.base.base import BaseSerializers


class EtatDetailSerializers(BaseSerializers):

    class Meta:
        model = Etat
        fields = ['index','nom','desc','url']