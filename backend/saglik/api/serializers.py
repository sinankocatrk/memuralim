from rest_framework import serializers
from saglik.models import *


class HemsireSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hemsire
        fields = '__all__'


