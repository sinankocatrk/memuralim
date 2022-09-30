from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
#from saglik.api.permissions import IsAdminUserOrReadOnly, IsYorumSahibiOrReadOnly
#from saglik.api.pagination import SmallPagination, LargePagination


from saglik.api.serializers import *
from saglik.models import *


class HemsireListCreateAPIView(ListModelMixin, CreateModelMixin,GenericAPIView):
    queryset = Hemsire.objects.all()
    serializer_class = HemsireSerializer
        # listelemek
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # yaratmak istiyorum
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



