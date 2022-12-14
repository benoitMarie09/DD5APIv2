from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from collections import OrderedDict


class BaseSerializers(ModelSerializer):
    url = serializers.SerializerMethodField()
    def get_url(self,obj):
       request = self.context.get('request')
       abs_url = obj.get_absolute_url()
       return request.build_absolute_uri(abs_url)
    def to_representation(self, instance):
        result = super(BaseSerializers, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] ])
