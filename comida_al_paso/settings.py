from pathlib import Path
import os
from datetime import timedelta
from dotenv import load_dotenv
import dj_database_url  # NUEVO IMPORT

# Cargar variables de entorno desde .env si existe
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-change-this-in-production')

# Environment
ENV = os.getenv('ENV', 'development').lower()

# DEBUG: False por defecto si estamos en Render
# Render define automáticamente la variable 'RENDER', usaremos eso para desactivar debug
DEBUG = 'RENDER' not in os.environ

# ALLOWED_HOSTS
ALLOWED_HOSTS = ['*'] # Se puede restringir luego a ['.onrender.com']

# Apps instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party apps
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',

    # Local apps
    'api',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # WhiteNoise: Debe ir justo después de SecurityMiddleware
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'comida_al_paso.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'comida_al_paso.wsgi.application'

# ---------------------------
# BASE DE DATOS (MODIFICADO PARA RENDER)
# ---------------------------

DATABASES = {
    'default': dj_database_url.config(
        # Busca automáticamente la variable DATABASE_URL (Render)
        # Si no la encuentra, usa SQLite localmente
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

# ---------------------------
# Validación de contraseñas
# ---------------------------

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# ---------------------------
# Internacionalización
# ---------------------------

LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'America/Argentina/Buenos_Aires'
USE_I18N = True
USE_TZ = True

# ---------------------------
# Archivos estáticos
# ---------------------------

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ---------------------------
# MEDIA
# ---------------------------

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ---------------------------
# CORS & CSRF (Configuración Lista para Despliegue)
# ---------------------------

CORS_ALLOW_ALL_ORIGINS = True # Permitimos acceso global inicialmente para evitar bloqueos
CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:5173',
    'http://127.0.0.1:5173',
    'https://*.onrender.com',
    'https://*.vercel.app',  # ← Frontend Vercel
]

# ---------------------------
# REST FRAMEWORK + JWT
# ---------------------------

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=int(os.getenv('JWT_ACCESS_TOKEN_LIFETIME', '60'))),
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=int(os.getenv('JWT_REFRESH_TOKEN_LIFETIME', '1440'))),
    'AUTH_HEADER_TYPES': ('Bearer',),
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ---------------------------
# LOGGING
# ---------------------------

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[{levelname}] {asctime} {name} - {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        'api': {
            'handlers': ['console'],
            'level': os.getenv('API_LOG_LEVEL', 'DEBUG'),
        },
    },
}

# ---------------------------
# SEGURIDAD EN PRODUCCIÓN
# ---------------------------

if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'