from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
#from saglik.api.permissions import IsAdminUserOrReadOnly, IsYorumSahibiOrReadOnly
#from saglik.api.pagination import SmallPagination, LargePagination

from rest_framework.settings import api_settings
from saglik.api.serializers import *
from saglik.models import *


# class HemsireListCreateAPIView(ListModelMixin, CreateModelMixin,GenericAPIView):
#     queryset = Hemsire.objects.all()
#     serializer_class = HemsireSerializer

#         # listelemek
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     # yaratmak istiyorum
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

    # filter_backends = api_settings.DEFAULT_FILTER_BACKENDS
    # def filter_queryset(self, queryset):

    #     for backend in list(self.filter_backends):
    #         queryset = backend().filter_queryset(self.request, queryset, self)
    #     return queryset

class EbeListCreateAPIView(ListModelMixin, CreateModelMixin,GenericAPIView):
    queryset = Yil2021.objects.filter(pozisyon__contains = "HEMŞİRE")
    serializer_class = Yil2021Serializer

        # listelemek
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # yaratmak istiyorum
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


