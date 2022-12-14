from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
 
from data.models import TypeDegat
from data.serializers import TypeDegatDetailSerializers, TypeDegatListSerializers

 
class TypeDegatViewset(ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    model = TypeDegat
    serializer_classes = {
        'list':TypeDegatListSerializers,
        'retrieve':TypeDegatDetailSerializers,
    }

    default_serializer_class = TypeDegatListSerializers

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return TypeDegat.objects.all()
 