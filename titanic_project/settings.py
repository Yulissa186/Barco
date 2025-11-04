from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY
SECRET_KEY = os.environ.get('SECRET_KEY', '123456789')  # usar variable de entorno en producción

# DEBUG
DEBUG = False  # Siempre False en Render

# Hosts permitidos
ALLOWED_HOSTS = ['analisisdat.onrender.com']

# Apps
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'titanic_app',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# URL principal
ROOT_URLCONF = 'titanic_project.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'titanic_app' / 'templates'],
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

# WSGI
WSGI_APPLICATION = 'titanic_project.wsgi.application'

# Base de datos SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Archivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # necesario para collectstatic en Render
STATICFILES_DIRS = [
    BASE_DIR / 'titanic_app' / 'static',
]

# Archivos media (opcional)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Zona horaria
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True
