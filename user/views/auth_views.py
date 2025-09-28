from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.utils import extend_schema

@extend_schema(tags=["Auth"])
class JwtTokenObtainPairView(TokenObtainPairView):
    """POST /api/auth/token/"""

@extend_schema(tags=["Auth"])
class JwtTokenRefreshView(TokenRefreshView):
    """POST /api/auth/refresh/"""
