from django_project.settings import *


SECRET_KEY = 'fake-key'
LOGGING = None
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.getenv('PGHOST', '127.0.0.1'),
        'PORT': int(os.getenv('PGPORT ', 5433)),
        'NAME': os.getenv('POSTGRES_DB', 'django'),
        'USER': os.getenv('POSTGRES_USER', 'django'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'django'),
        'TEST': {
            'NAME': 'test_django'
        }
    }
}
