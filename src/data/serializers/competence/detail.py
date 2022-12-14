from data.models import Competence
from data.serializers.base.base import BaseSerializers


class CompetenceDetailSerializers(BaseSerializers):
 
    class Meta:
        model = Competence
        fields = '__all__'