from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
 
from data.models import Sort, EcoleMagie
from data.serializers import SortListSerializers, SortDetailSerializers, EcoleMagieListSerializers, EcoleMagieDetailSerializers


class SortViewset(ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = Sort
    serializer_classes = {
        'list':SortListSerializers,
        'retrieve':SortDetailSerializers,
    }

    default_serializer_class = SortListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return Sort.objects.all()


class EcoleMagieViewset(ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = EcoleMagie
    serializer_classes = {
        'list':EcoleMagieListSerializers,
        'retrieve':EcoleMagieDetailSerializers,
    }

    default_serializer_class = SortListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return EcoleMagie.objects.all()