# Pomocné funkce specifické pro správu událostí.
from datetime import datetime

def is_event_past(event_date):
    return event_date < datetime.now()
