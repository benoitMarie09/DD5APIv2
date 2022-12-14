from rest_framework.serializers import ModelSerializer, StringRelatedField
from data.serializers.base.base import BaseSerializers
from data.models import TypeDegat, DegatSortNiveaux, DegatSortEmplacements, SoinSortEmplacements


class TypeDegatDetailSerializers(BaseSerializers):
 
    class Meta:
        model = TypeDegat
        fields = ['index','nom','desc','url']


class DegatSortNiveauxSerializer(BaseSerializers):
    niveau_0 = StringRelatedField(many=True)
    niveau_5 = StringRelatedField(many=True)
    niveau_11 = StringRelatedField(many=True)
    niveau_17 = StringRelatedField(many=True)
    class Meta:
        model = DegatSortNiveaux
        fields = ['desc','niveau_0','niveau_5','niveau_11','niveau_17',]

class DegatSortEmplacementsSerializer(ModelSerializer):
    emplacement_nv0 = StringRelatedField(many=True)
    emplacement_nv1 = StringRelatedField(many=True)
    emplacement_nv2 = StringRelatedField(many=True)
    emplacement_nv3 = StringRelatedField(many=True)
    emplacement_nv4 = StringRelatedField(many=True)
    emplacement_nv5 = StringRelatedField(many=True)
    emplacement_nv6 = StringRelatedField(many=True)
    emplacement_nv7 = StringRelatedField(many=True)
    emplacement_nv8 = StringRelatedField(many=True)
    emplacement_nv9 = StringRelatedField(many=True)
    class Meta:
        model = DegatSortEmplacements
        fields = ['desc','emplacement_nv0','emplacement_nv1','emplacement_nv2','emplacement_nv3','emplacement_nv4','emplacement_nv5','emplacement_nv6','emplacement_nv7','emplacement_nv8','emplacement_nv9',]

class SoinSortEmplacementsSerializer(BaseSerializers):
    emplacement_nv0 = StringRelatedField(many=True)
    emplacement_nv1 = StringRelatedField(many=True)
    emplacement_nv2 = StringRelatedField(many=True)
    emplacement_nv3 = StringRelatedField(many=True)
    emplacement_nv4 = StringRelatedField(many=True)
    emplacement_nv5 = StringRelatedField(many=True)
    emplacement_nv6 = StringRelatedField(many=True)
    emplacement_nv7 = StringRelatedField(many=True)
    emplacement_nv8 = StringRelatedField(many=True)
    emplacement_nv9 = StringRelatedField(many=True)
    class Meta:
        model = SoinSortEmplacements
        fields = ['desc','emplacement_nv0','emplacement_nv1','emplacement_nv2','emplacement_nv3','emplacement_nv4','emplacement_nv5','emplacement_nv6','emplacement_nv7','emplacement_nv8','emplacement_nv9',]

