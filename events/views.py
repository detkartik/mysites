from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EventSerializer
from .models import Event
from rest_framework.authentication import TokenAuthentication

# Create your views here.


class EventViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = Event.objects.all().order_by('id')
    serializer_class = EventSerializer
