from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
 
from data.models import Race, SousRace, Trait
from data.serializers import RaceListSerializers, RaceDetailSerializers, SousRaceListSerializers, SousRaceDetailSerializers,TraitDetailSerializers, TraitListSerializers, MaitriseListSerializers, OptionListSerializer, RaceMaitrisesOptionsList
 

class RaceViewset(ReadOnlyModelViewSet):

    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = Race
    serializer_classes = {
        'list':RaceListSerializers,
        'retrieve':RaceDetailSerializers,
    }

    default_serializer_class = RaceListSerializers

    @action(detail=True,url_path='sous-races', url_name='sous-races')
    def sous_races(self, request,pk=None):
        race = self.get_object()
        sous_races = race.sous_race.all()
        serializers =SousRaceListSerializers(sous_races,context = {'request':request}, many=True)
        return Response(serializers.data)

    @action(detail=True,url_path='traits', url_name='traits')
    def traits(self, request,pk=None):
        race = self.get_object()
        traits = race.traits.all()
        serializers =TraitListSerializers(traits,context = {'request':request}, many=True)
        return Response(serializers.data)

    @action(detail=True,url_path='maitrises', url_name='maitrises')
    def maitrises(self, request,pk=None):
        race = self.get_object()
        maitrises = race.maitrises_depart.all()
        serializers1 =MaitriseListSerializers(maitrises,context = {'request':request}, many=True)
        maitrises_options = race.maitrises_option
        serializers2 = OptionListSerializer(maitrises_options,context = {'request':request})
        serializers = RaceMaitrisesOptionsList(race,context = {'request':request})
        return Response(serializers.data)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return Race.objects.filter(parent_race=True).select_subclasses()

class SousRaceViewset(ReadOnlyModelViewSet):

    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = SousRace
    serializer_classes = {
        'list':SousRaceListSerializers,
        'retrieve':SousRaceDetailSerializers,
    }

    default_serializer_class = SousRaceListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return SousRace.objects.all()
 


class TraitViewset(ReadOnlyModelViewSet):

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['race']

    model = Trait
    serializer_classes = {
        'list':TraitListSerializers,
        'retrieve':TraitDetailSerializers,
    }

    default_serializer_class = TraitListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return Trait.objects.all()