from data.serializers.base.base import BaseSerializers
from data.models import Don 


class DonSerializers(BaseSerializers):
 
    class Meta:
        model = Don
        fields = '__all__'