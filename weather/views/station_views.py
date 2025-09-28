from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from drf_spectacular.utils import extend_schema_view, extend_schema

from weather.models.station import Station
from weather.serializers.station_serializers import StationSerializer

@extend_schema_view(
    list=extend_schema(tags=["Weather - Stations"]),
    retrieve=extend_schema(tags=["Weather - Stations"]),
    create=extend_schema(tags=["Weather - Stations"]),
    update=extend_schema(tags=["Weather - Stations"]),
    partial_update=extend_schema(tags=["Weather - Stations"]),
    destroy=extend_schema(tags=["Weather - Stations"]),
)
class StationViewSet(ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    search_fields = ["name"]
    ordering_fields = ["name", "created_at"]
    ordering = ["name"]
