from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
 
from data.models import Regle, RegleSousSection
from data.serializers import RegleSerializers, RegleSousSectionSerializers

 
class RegleViewset(ReadOnlyModelViewSet):

    serializer_class = RegleSerializers

    def get_queryset(self):
        return Regle.objects.all()
 
class RegleSousSectionViewset(ReadOnlyModelViewSet):

    serializer_class = RegleSousSectionSerializers

    def get_queryset(self):
        return RegleSousSection.objects.all()