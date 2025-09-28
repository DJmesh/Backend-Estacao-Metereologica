from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

@extend_schema(
    tags=["Core"],
    auth=[],
    summary="Health check",
    description="Endpoint público de verificação de saúde do serviço.",
)
class HealthView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return Response({"status": "ok"})
