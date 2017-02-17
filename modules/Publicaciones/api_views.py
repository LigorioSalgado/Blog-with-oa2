from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Publicacion
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework import generics


class PublicacionList(generics.ListCreateAPIView):

    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer

class PublicacionDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer
