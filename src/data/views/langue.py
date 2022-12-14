from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
 
from data.models import Langue
from data.serializers import LangueListSerializers, LangueDetailSerializers
 
 
class LangueViewset(ReadOnlyModelViewSet):

    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = Langue
    serializer_classes = {
        'list':LangueListSerializers,
        'retrieve':LangueDetailSerializers,
    }

    default_serializer_class = LangueListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return Langue.objects.all()