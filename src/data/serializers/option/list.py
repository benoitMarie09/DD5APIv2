from data.serializers.base.base import BaseSerializers
from data.serializers.caracteristique.list import CaracteristiqueListSerializers
from data.serializers.competence.list import CompetenceListSerializers
from data.serializers.equipement.list import EquipementListSerializers
from data.serializers.langue.list import LangueListSerializers
from data.serializers.maitrise.list import MaitriseListSerializers
from data.models import Option


class OptionListSerializer(BaseSerializers):
    caracteristiques = CaracteristiqueListSerializers(many=True)
    competences = CompetenceListSerializers(many=True)
    maitrises = MaitriseListSerializers(many=True)
    langues = LangueListSerializers(many=True)
    equipements = EquipementListSerializers(many=True)
    
    class Meta:
        model=Option
        fields = ['nom','desc','nombre_choix','caracteristiques','competences','maitrises','langues','equipements']

