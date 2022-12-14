from data.serializers.base.base import BaseSerializers
from data.models import Competence


class CompetenceListSerializers(BaseSerializers):
 
    class Meta:
        model = Competence
        fields = ['index','nom','url']

