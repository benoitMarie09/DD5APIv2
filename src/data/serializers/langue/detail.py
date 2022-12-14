from data.serializers.base.base import BaseSerializers
from data.models import Langue


class LangueDetailSerializers(BaseSerializers):
 
    class Meta:
        model = Langue
        fields = ['index','nom','type','desc','race_typiques','url']

