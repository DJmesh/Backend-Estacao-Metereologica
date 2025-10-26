from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers.register import (
    RegisterRequestSerializer,
    RegisterResponseSerializer,
    RegisterCreateSerializer,
)

@extend_schema(
    tags=["Users"],
    request=RegisterRequestSerializer,
    responses={201: RegisterResponseSerializer},
    examples=[
        OpenApiExample(
            "Exemplo de registro",
            value={
                "username": "edudu",
                "email": "eduardo@example.com",
                "first_name": "Eduardo",
                "last_name": "Prestes",
                "password": "S3gura&F0rte",
                "password_confirm": "S3gura&F0rte",
            },
        )
    ],
)
class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        # valida payload de entrada (aparece no Swagger)
        req = RegisterRequestSerializer(data=request.data)
        req.is_valid(raise_exception=True)

        # cria usuário (sem vazar no schema)
        creator = RegisterCreateSerializer()
        user = creator.create(dict(req.validated_data))

        # serializa resposta (aparece no Swagger)
        return Response(RegisterResponseSerializer(user).data, status=status.HTTP_201_CREATED)
