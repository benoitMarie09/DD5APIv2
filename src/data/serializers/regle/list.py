from data.serializers.base.base import BaseSerializers
from data.models import Regle, RegleSousSection


class RegleSerializers(BaseSerializers):
 
    class Meta:
        model = Regle
        fields = '__all__'

class RegleSousSectionSerializers(BaseSerializers):
 
    class Meta:
        model = RegleSousSection
        fields = '__all__'

