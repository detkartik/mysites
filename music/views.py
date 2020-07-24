from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Songs
from .serializers import SongsSerializer
from rest_framework.authentication import TokenAuthentication


class ListSongsView(viewsets.ModelViewSet):
    """
    Provides a get method handler.
    """
    authentication_classes = (TokenAuthentication,)
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
