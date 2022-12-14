from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
 
from data.models import Etat
from data.serializers import EtatListSerializers, EtatDetailSerializers

 
class EtatViewset(ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = Etat
    serializer_classes = {
        'list':EtatListSerializers,
        'retrieve':EtatDetailSerializers,
    }

    default_serializer_class = EtatListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return Etat.objects.all()