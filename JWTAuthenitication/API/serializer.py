from rest_framework.serializers import  ModelSerializer
from API.models import *


class CoderSerializer(ModelSerializer):
    class Meta:
        model=CODERS
        fields="__all__"