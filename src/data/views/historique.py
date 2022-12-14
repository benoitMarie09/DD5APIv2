from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
 
from data.models import Historique
from data.serializers import HistoriqueListSerializers, HistoriqueDetailSerializers

class HistoriqueViewset(ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = Historique
    serializer_classes = {
        'list':HistoriqueListSerializers,
        'retrieve':HistoriqueDetailSerializers,
    }

    default_serializer_class = HistoriqueListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return Historique.objects.all()