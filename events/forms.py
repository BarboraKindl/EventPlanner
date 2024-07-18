from django import forms
from .models import Event, Location, Resource

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_time', 'end_time', 'location', 'resources']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'address']

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'description']
