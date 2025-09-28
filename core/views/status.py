from django.conf import settings
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

@extend_schema(
    tags=["Core"],
    summary="Status da aplicação",
    description="Retorna informações básicas da aplicação. Requer JWT.",
)
class StatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        version = None
        try:
            version = settings.SPECTACULAR_SETTINGS.get("VERSION")
        except Exception:
            version = None

        return Response({
            "app": "Meteo Station API",
            "version": version,
            "user": request.user.username,
            "is_authenticated": request.user.is_authenticated,
        })
