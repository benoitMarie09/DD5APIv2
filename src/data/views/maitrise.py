from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
 
from data.models import Maitrise
from data.serializers import MaitriseListSerializers, MaitriseDetailSerializers
 

class MaitriseViewset(ReadOnlyModelViewSet):

    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = Maitrise
    serializer_classes = {
        'list':MaitriseListSerializers,
        'retrieve':MaitriseDetailSerializers,
    }

    default_serializer_class = MaitriseListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return Maitrise.objects.all()
 