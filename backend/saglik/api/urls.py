from django.urls import path
from saglik.api import views as api_views

urlpatterns = [
   path('saglik/',api_views.HemsireListCreateAPIView.as_view(), name='saglik-listesi' ),
   #path('saglik/<int:pk>', api_views.HemsireDetailAPIView.as_view(), name='saglik-bilgileri'),


]