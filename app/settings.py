from pathlib import Path
from datetime import timedelta
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-afn#(8z&dsp(89ogh3!7t@$q@xv^2(uf%b@*xiigzug8wdcv=8",
)
DEBUG = os.getenv("DJANGO_DEBUG", "0") == "1"
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "*").split(",")

INSTALLED_APPS = [
    # Theme
    "jazzmin",

    # Django core
    "corsheaders",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party
    "rest_framework",
    "drf_spectacular",
    "django_filters",

    # Local apps
    "base",
    "core",
    "user",
    "weather",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware", 
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# WhiteNoise (arquivos estáticos comprimidos com hash)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

CORS_ALLOWED_ORIGINS = [
    "https://meteo-station-api.onrender.com/",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    "https://meteo-station-api.onrender.com/",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# Em desenvolvimento, se quiser liberar tudo (NÃO use em produção):
# CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "app.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.getenv("DB_NAME", BASE_DIR / "db.sqlite3"),
        "USER": os.getenv("DB_USER", ""),
        "PASSWORD": os.getenv("DB_PASSWORD", ""),
        "HOST": os.getenv("DB_HOST", ""),
        "PORT": os.getenv("DB_PORT", ""),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = "/static/"

# Diretório-fonte (onde está admin/css, admin/js, etc)
STATICFILES_DIRS = [ BASE_DIR / "static" ]

# Diretório de saída da coleta
STATIC_ROOT = BASE_DIR / "static_collected"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Custom user model
AUTH_USER_MODEL = "user.User"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.OrderingFilter",
        "rest_framework.filters.SearchFilter",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
}

# app/settings.py

SPECTACULAR_SETTINGS = {
    "TITLE": "Meteo Station API",
    "DESCRIPTION": "Weather station backend (humidity, temperature, wind, rain, luminosity).",
    "VERSION": "1.0.0",
    "SERVERS": [
        {"url": "http://localhost:8000"},
        {"url": "http://127.0.0.1:8000"},
    ],
    "SWAGGER_UI_SETTINGS": {"persistAuthorization": True},
    "COMPONENT_SPLIT_REQUEST": True,
    "SECURITY": [{"BearerAuth": []}],
    "COMPONENTS": {
        "securitySchemes": {
            "BearerAuth": {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
        }
    },
    "TAGS": [
        {"name": "Auth", "description": "JWT authentication endpoints."},
        {"name": "Core", "description": "Core endpoints (health, status)."},
        {"name": "Weather - Stations", "description": "Manage weather stations."},
        {"name": "Weather - Readings", "description": "Manage sensor readings."},
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "SIGNING_KEY": SECRET_KEY,
    "AUTH_HEADER_TYPES": ("Bearer",),
}

JAZZMIN_SETTINGS = {
    "site_title": "Meteo Admin",
    "site_header": "Meteo Admin",
    "site_brand": "Meteo Station",
    "site_logo": "admin/img/logo-leaf.svg",
    "login_logo": "admin/img/logo-leaf.svg",
    "welcome_sign": "Bem-vindo ao Meteo Admin",
    "show_ui_builder": False,
    "topmenu_links": [
        {"name": "Documentação", "url": "swagger-ui", "permissions": ["auth.view_user"]},
        {"name": "Health", "url": "core:health", "permissions": []},
    ],
    "icons": {
        "user.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "weather.Station": "fas fa-leaf",
        "weather.Reading": "fas fa-cloud-sun",
    },
    "custom_css": ["admin/css/green-theme.css"],
    "custom_js": ["admin/js/lucide-jazzmin.js"],
}

JAZZMIN_UI_TWEAKS = {
    "theme": "minty",
    "dark_mode_theme": "darkly",
    "navbar": "navbar-success navbar-dark",
    "no_navbar_border": True,
    "sidebar": "sidebar-dark-success",
    "sidebar_nav_flat_style": True,
    "sidebar_nav_child_indent": True,
    "related_modal_active": True,
    "brand_colour": "navbar-success",
    "accent": "accent-success",
    "button_classes": {
        "primary": "btn-success",
        "secondary": "btn-outline-success",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
}
