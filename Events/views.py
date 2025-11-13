from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all().order_by('-event_date')
        event_date = self.request.query_params.get('date')

        if event_date:
            queryset = queryset.filter(event_date=event_date)

        return queryset
