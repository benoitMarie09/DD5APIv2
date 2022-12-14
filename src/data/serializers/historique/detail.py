from rest_framework import serializers
from data.models import Historique
from data.serializers.base.base import BaseSerializers
from data.serializers.competence.list import CompetenceListSerializers
from data.serializers.equipement.list import EquipementListSerializers
from data.serializers.maitrise.list import MaitriseListSerializers
from data.serializers.option.list import OptionListSerializer


class HistoriqueDetailSerializers(BaseSerializers):
    maitrises_depart = MaitriseListSerializers(many=True)
    langues_options = OptionListSerializer()
    maitrises_options =OptionListSerializer()
    equipements_options =OptionListSerializer()
    competences = CompetenceListSerializers(many=True)
    equipements_depart = EquipementListSerializers(many=True)
    monaie_de_depart = serializers.StringRelatedField(many=True)
    class Meta:
        model = Historique
        fields = ['index','nom','desc','maitrises_depart','maitrises_options','competences','langues_options','equipements_depart','equipements_options','monaie_de_depart','url']
        depth = 1