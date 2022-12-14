from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
 
from data.models import Alignement
from data.serializers import AlignementListSerializers, AlignementDetailSerializers


class AlignementViewset(ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = Alignement
    serializer_classes = {
        'list':AlignementListSerializers,
        'retrieve':AlignementDetailSerializers,
    }

    default_serializer_class = AlignementListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return Alignement.objects.all()