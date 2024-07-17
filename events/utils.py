from django.utils import timezone
from .models import Resource

def is_event_upcoming(event):
    return event.start_time > timezone.now()

def get_available_resources(event):
    return Resource.objects.exclude(event=event)

def get_event_duration(event):
    return event.end_time - event.start_time
