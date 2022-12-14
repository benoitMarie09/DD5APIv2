from data.serializers.base.base import BaseSerializers
from data.models import Alignement

        
class AlignementDetailSerializers(BaseSerializers):
 
    class Meta:
        model = Alignement
        fields = '__all__'
