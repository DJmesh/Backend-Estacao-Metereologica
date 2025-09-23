from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models.user import User
from user.serializers.user_serializers import UserSerializer, MeSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return request.user and request.user.is_authenticated
        return request.user and request.user.is_staff

class UserViewSet(viewsets.ModelViewSet):
    """
    Gestão de usuários.
    - Listar/recuperar: qualquer autenticado
    - Criar/editar/deletar: somente staff
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ["username", "email"]
    ordering_fields = ["username", "date_joined"]

class MeView(APIView):
    """
    Retorna dados do usuário autenticado.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(MeSerializer(request.user).data)
