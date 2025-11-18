from pathlib import Path
from datetime import timedelta

# ==========================================================
# BASE DIR
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================================================
# SEGURIDAD
# ==========================================================

SECRET_KEY = 'CAMBIA_ESTA_CLAVE_EN_PRODUCCION'

DEBUG = True

ALLOWED_HOSTS = ['*']  # En desarrollo no hay problema

# ==========================================================
# APPS INSTALADAS
# ==========================================================

INSTALLED_APPS = [
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Terceros
    'rest_framework',
    'rest_framework_simplejwt',
    'django_filters',
    'drf_spectacular',  # ← SOLO UNA LIBRERÍA DE DOCUMENTACIÓN

    # App local
    'transporte',
]

# ==========================================================
# MIDDLEWARE
# ==========================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ==========================================================
# URLS / TEMPLATES / WSGI
# ==========================================================

ROOT_URLCONF = 'logistica.urls'

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

WSGI_APPLICATION = 'logistica.wsgi.application'

# ==========================================================
# BASE DE DATOS — DESARROLLO LOCAL (SQLite)
# ==========================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'logistica_db', 
        'USER': 'logistica_user',
        'PASSWORD': 'maldonado4321', 
        'HOST': '172.31.71.227', # <--- ¡PEGA AQUÍ LA IP PRIVADA!
        'PORT': '5432',
    }
}

# ==========================================================
# REST FRAMEWORK / JWT / SPECTACULAR
# ==========================================================

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# Configuración drf_spectacular
SPECTACULAR_SETTINGS = {
    'TITLE': 'Logística Global API',
    'DESCRIPTION': 'Sistema de gestión de transporte terrestre y aéreo',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,
}

# ==========================================================
# VALIDACIÓN DE CONTRASEÑAS
# ==========================================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ==========================================================
# INTERNACIONALIZACIÓN
# ==========================================================

LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_TZ = True

# ==========================================================
# STATIC / MEDIA FILES
# ==========================================================

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static_root'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ==========================================================
# AUTO FIELD
# ==========================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==========================================================
# LOGIN/LOGOUT REDIRECTS
# ==========================================================

LOGIN_URL = '/transporte/login/'
LOGIN_REDIRECT_URL = '/transporte/dashboard/'
LOGOUT_REDIRECT_URL = '/transporte/login/'