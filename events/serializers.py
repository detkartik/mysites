from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'day', 'start_time', 'end_time', 'notes')
