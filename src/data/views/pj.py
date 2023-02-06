from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
 
from data.models import PJ
from data.serializers import PJDetailSerializers, PJListSerializers
 

class PJViewset(ModelViewSet):

    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = PJ
    serializer_classes = {
        'list':PJListSerializers,
        'retrieve':PJDetailSerializers,
        'create':PJDetailSerializers,
    }

    default_serializer_class = PJListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return PJ.objects.all()
 