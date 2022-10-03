from rest_framework import serializers
from sqlalchemy import null
from saglik.models import *



# class HemsireSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Hemsire
#         fields = '__all__'

class GenelPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Saglik
        fields = '__all__'

class HemsireSerializer(GenelPostSerializer):

    class Meta:
        model = Hemsire
        fields = '__all__'

class EbeSerializer(GenelPostSerializer):
    
    class Meta:
        model = Ebe
        fields = '__all__'

class Yil2021Serializer(GenelPostSerializer):
    
    class Meta:
        model = Yil2021
        fields = '__all__'
