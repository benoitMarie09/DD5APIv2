from data.serializers.base.base import BaseSerializers
from data.models import Historique


class HistoriqueListSerializers(BaseSerializers):

    class Meta:
        model = Historique
        fields = ['index','nom','url']

