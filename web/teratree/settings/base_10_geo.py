from .base_09_wagtail import *

# Override the default database setting
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
print('Overriding the engine to use postgis://')

for app in [
    'django.contrib.admin',
    'django.contrib.gis',
]:
    if app not in INSTALLED_APPS:
        INSTALLED_APPS.append(app)

