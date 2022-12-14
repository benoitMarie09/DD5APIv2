from data.serializers.base.base import BaseSerializers
from data.models import Equipement, CategorieEquipement, Arme, Armure, Sac, EquipementAventurier, Vehicule, ProprieteArme



class EquipementListSerializers(BaseSerializers):
    class Meta:
        model = Equipement
        fields = ['index','nom','url']
        
    def to_representation(self, instance): 
        if isinstance(instance, Arme):
            return ArmeListSerializers(instance, context=self.context).to_representation(instance)
        elif isinstance(instance, Armure):
            return ArmureListSerializers(instance, context=self.context).to_representation(instance)
        elif isinstance(instance, EquipementAventurier):
            return EquipementAventurierListSerializers(instance, context=self.context).to_representation(instance)
        elif isinstance(instance, Sac):
            return SacListSerializers(instance, context=self.context).to_representation(instance)
        else:
            return super(EquipementListSerializers, self).to_representation(instance)
    

class CategorieEquipementListSerializers(BaseSerializers):

    class Meta:
        model = CategorieEquipement
        fields = ['index','nom','url']


class ProprieteArmeListSerializers(BaseSerializers):
    class Meta:
        model = ProprieteArme
        fields = ['index','nom','url']

class ArmeListSerializers(BaseSerializers):
    
    class Meta:
        model = Arme
        fields = ['index','nom','url']

class EquipementAventurierListSerializers(BaseSerializers):
    
    class Meta:
        model = EquipementAventurier
        fields = ['index','nom','url']

class SacListSerializers(BaseSerializers):
    
    class Meta:
        model = Sac
        fields = ['index','nom','url']
        
class ArmureListSerializers(BaseSerializers): 
    class Meta:
        model = Armure
        fields = ['index','nom','url']


class VehiculeListSerializers(BaseSerializers):
    class Meta:
        model = Vehicule
        fields = ['index','nom','url']

