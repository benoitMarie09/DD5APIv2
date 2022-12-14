from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
 
from data.models import Competence
from data.serializers import CompetenceListSerializers, CompetenceDetailSerializers

 
class CompetenceViewset(ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = Competence
    serializer_classes = {
        'list':CompetenceListSerializers,
        'retrieve':CompetenceDetailSerializers,
    }

    default_serializer_class = CompetenceListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return Competence.objects.all()