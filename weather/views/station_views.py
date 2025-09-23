from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.decorators import action
from rest_framework.response import Response

from weather.models.station import Station
from weather.models.reading import Reading
from weather.serializers.station_serializers import StationSerializer
from weather.serializers.reading_serializers import ReadingSerializer

class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["is_active"]
    search_fields = ["name", "description"]
    ordering_fields = ["name", "created_at", "updated_at"]

    @action(detail=True, methods=["get"], url_path="latest-reading")
    def latest_reading(self, request, pk=None):
        station = self.get_object()
        reading = Reading.objects.filter(station=station).order_by("-measured_at", "-created_at").first()
        if not reading:
            return Response({"detail": "Sem leituras para esta estação."}, status=404)
        return Response(ReadingSerializer(reading).data)
