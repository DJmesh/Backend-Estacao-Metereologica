from django.utils.dateparse import parse_datetime
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from weather.models.reading import Reading
from weather.serializers.reading_serializers import ReadingSerializer

class ReadingViewSet(viewsets.ModelViewSet):
    queryset = Reading.objects.select_related("station").all()
    serializer_class = ReadingSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["station"]
    search_fields = ["station__name"]
    ordering_fields = ["created_at", "measured_at", "temperature", "humidity", "wind_speed", "rain_mm", "luminosity"]

    def get_queryset(self):
        qs = super().get_queryset()
        c_after = self.request.query_params.get("created_after")
        c_before = self.request.query_params.get("created_before")
        m_after = self.request.query_params.get("measured_after")
        m_before = self.request.query_params.get("measured_before")

        if c_after:
            dt = parse_datetime(c_after)
            if dt:
                qs = qs.filter(created_at__gte=dt)
        if c_before:
            dt = parse_datetime(c_before)
            if dt:
                qs = qs.filter(created_at__lte=dt)
        if m_after:
            dt = parse_datetime(m_after)
            if dt:
                qs = qs.filter(measured_at__gte=dt)
        if m_before:
            dt = parse_datetime(m_before)
            if dt:
                qs = qs.filter(measured_at__lte=dt)
        return qs
