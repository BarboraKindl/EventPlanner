# Serializátory pro modely (např. pro REST API).
from rest_framework import serializers
from applications.events.models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
