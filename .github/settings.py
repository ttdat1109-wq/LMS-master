import os
from decouple import config
import dj_database_url

# SECRET_KEY
SECRET_KEY = config('SECRET_KEY', default='unsafe-secret-key')

# DEBUG
DEBUG = config('DEBUG', default=False, cast=bool)

# Database
DATABASES = {
    'default': dj_database_url.config(default=f'sqlite:///{os.path.join(BASE_DIR, "db.sqlite3")}')
}

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
