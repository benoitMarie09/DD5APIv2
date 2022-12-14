from rest_framework import serializers
from data.models import Race, Option, Incantation, Trait, Niveau
from data.serializers.base.base import BaseSerializers
from data.serializers.caracteristique.list import CaracteristiqueListSerializers
from data.serializers.classe.list import CapaciteListSerializers, InfoListSerializers, PackEquipementClasseListSerializers
from data.serializers.field import EmplacementSortField, SpecifiqueField
from data.serializers.langue.list import LangueListSerializers
from data.serializers.maitrise.list import MaitriseListSerializers
from data.serializers.option.list import OptionListSerializer
from data.serializers.race.list import RaceListSerializers, SousRaceListSerializers, TraitListSerializers
from data.serializers.sort.list import SortListSerializers

class RaceDetailSerializers(BaseSerializers):
    sous_race = SousRaceListSerializers(many=True)
    caracteristique = serializers.StringRelatedField(many=True)
    maitrises_depart = MaitriseListSerializers(many=True)
    langues = LangueListSerializers(many=True)
    taille = serializers.StringRelatedField()
    traits = TraitListSerializers(many=True)
    maitrises_option = OptionListSerializer()
    langues_option = OptionListSerializer()
    sorts_option = OptionListSerializer()
    bonus_caracteristique_option = OptionListSerializer()
    class Meta:
        model = Race
        fields = ['index','nom','vitesse','caracteristique','bonus_caracteristique_option','age','poids','taille','taille_details','maitrises_depart','maitrises_option','langues','langues_option','langues_desc','traits','sorts','sorts_option','sous_race','url',]
        depth = 2



class OptionPackDetailSerializer(OptionListSerializer):
    packs_equipements = PackEquipementClasseListSerializers(many=True)
    class Meta:
        model=Option
        fields = ['desc','nombre_choix','packs_equipements']


class IncantationDetailSerializers(BaseSerializers):
    info = InfoListSerializers(many=True)
    caracteristique = CaracteristiqueListSerializers()
    class Meta:
        model = Incantation
        fields = ['nom','caracteristique','info']


class NiveauDetailSerializers(BaseSerializers):
    capacite = CapaciteListSerializers(many=True)
    emplacements_sorts = EmplacementSortField(read_only = True)
    specifique = SpecifiqueField(many=True, read_only = True)

    class Meta:
        model = Niveau
        fields = ['index', 'nom','niveau','bonus_maitrise','capacite','emplacements_sorts','specifique','url']


class TraitDetailSerializers(BaseSerializers):
    race = RaceListSerializers(many = True)
    class Meta:
        model = Trait
        fields = ['index','nom','desc','race','url']

class SousRaceDetailSerializers(BaseSerializers):
    race = RaceListSerializers()
    caracteristique = serializers.StringRelatedField(many=True)
    maitrises_depart = MaitriseListSerializers(many=True)
    maitrises_option = OptionListSerializer()
    langues = LangueListSerializers(many=True)
    langues_option = OptionListSerializer()
    taille = serializers.StringRelatedField()
    traits = TraitListSerializers(many=True)
    sorts = SortListSerializers(many=True)
    sorts_option = OptionListSerializer()
    class Meta:
        model = Race
        fields = ['index','nom','race','vitesse','caracteristique','bonus_caracteristique_option','age','poids','taille','taille_details','maitrises_depart','maitrises_option','langues','langues_option','langues_desc','traits','sorts','sorts_option','url',]
        depth = 2
   

