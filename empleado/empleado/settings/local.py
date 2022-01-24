from .base import * # . indicates that the script is in the same file
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER':'josue',
        'PASSWORD': '', # ADD PASSWORD
        'HOST': 'localhost',
        'PORT': '5432',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        # 'NAME': BASE_DIR.child('db.sqlite3'), # use this If got a TypeError: unsupported operand type(s) for /: 'Path' and 'str'
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
