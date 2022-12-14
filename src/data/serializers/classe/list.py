
from data.serializers.base.base import BaseSerializers
from data.serializers.option.list import OptionListSerializer
from data.models import Classe, PackEquipementClasse, Info, SousClasse, Capacite
from data.serializers.field import ContenuField




class ClasseListSerializers(BaseSerializers):
 
    class Meta:
        model = Classe
        fields = ['index','nom','url']


class NiveauListSerializers(BaseSerializers):
    class Meta:
        model = Classe
        fields = ['index','nom','url']


class PackEquipementClasseListSerializers(BaseSerializers):
    contenu_pack =ContenuField(many=True,read_only = True)
    options = OptionListSerializer(many=True)
    class Meta:
        model=PackEquipementClasse
        fields = ['index', 'nom', 'desc', 'contenu_pack', 'options']


class InfoListSerializers(BaseSerializers):
 
    class Meta:
        model = Info
        fields = ['nom','desc']


class SousClasseListSerializers(BaseSerializers):
 
    class Meta:
        model = SousClasse
        fields = ['index','nom','url']


class CapaciteListSerializers(BaseSerializers):
 
    class Meta:
        model = Capacite
        fields = ['index','nom','url']
