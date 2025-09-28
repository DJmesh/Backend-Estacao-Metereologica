from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from drf_spectacular.utils import extend_schema_view, extend_schema

from weather.models.reading import Reading
from weather.serializers.reading_serializers import ReadingSerializer

@extend_schema_view(
    list=extend_schema(tags=["Weather - Readings"]),
    retrieve=extend_schema(tags=["Weather - Readings"]),
    create=extend_schema(tags=["Weather - Readings"]),
    update=extend_schema(tags=["Weather - Readings"]),
    partial_update=extend_schema(tags=["Weather - Readings"]),
    destroy=extend_schema(tags=["Weather - Readings"]),
)
class ReadingViewSet(ModelViewSet):
    queryset = Reading.objects.select_related("station").all()
    serializer_class = ReadingSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ["station"]
    ordering_fields = ["created_at", "measured_at"]
    ordering = ["-created_at"]
