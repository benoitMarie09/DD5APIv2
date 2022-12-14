from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
 
from data.models import Don
from data.serializers import DonSerializers

 
class DonViewset(ReadOnlyModelViewSet):

    serializer_class = DonSerializers

    def get_queryset(self):
        return Don.objects.all()