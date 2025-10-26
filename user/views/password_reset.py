from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiExample

from user.serializers.password_reset import (
    PasswordResetRequestSerializer,
    PasswordResetConfirmSerializer,
)

@extend_schema(
    tags=["Users"],
    request=PasswordResetRequestSerializer,
    responses={200: PasswordResetRequestSerializer},
    examples=[
        OpenApiExample(
            "Solicitação de reset",
            value={"email": "usuario@example.com"},
        )
    ],
)
class PasswordResetRequestView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        s = PasswordResetRequestSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        result = s.create(s.validated_data)
        return Response(result, status=status.HTTP_200_OK)


@extend_schema(
    tags=["Users"],
    request=PasswordResetConfirmSerializer,
    responses={200: PasswordResetConfirmSerializer},
    examples=[
        OpenApiExample(
            "Confirmação de reset",
            value={
                "uid": "Mg",  # exemplo
                "token": "asx2d1-abc...",
                "new_password": "NovaSenha@123",
                "new_password_confirm": "NovaSenha@123",
            },
        )
    ],
)
class PasswordResetConfirmView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        s = PasswordResetConfirmSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        result = s.save()
        return Response(result, status=status.HTTP_200_OK)
