import os

SECRET_KEY = os.getenv('TAIGA_SECRET_KEY', '9%pno@m688el28@2+^y4v^&6wluqk-g#j#d7$dsjtht)o30dn1')

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    os.getenv('TAIGA_ALLOWED_HOST', 'localhost'),
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('TAIGA_DB_NAME', 'taiga'),
        'USER': os.getenv('TAIGA_DB_USER', 'taiga'),
        'PASSWORD': os.getenv('TAIGA_DB_PASSWORD', 'changeme'),
        'HOST': os.getenv('TAIGA_DB_HOST', 'database'),
        'PORT': os.getenv('TAIGA_DB_PORT', '5432'),
    }
}

EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
EVENTS_PUSH_BACKEND_OPTIONS = {"url": "amqp://guest:guest@broker/taiga"}
