from .base_99_last import *

MEDIA_ROOT = os.path.join(ROOT_DIR, 'media')
MEDIA_URL = '/media/'
DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'
print(os.environ.get('DEBUG'), '=>', DEBUG)
ALLOWED_HOSTS = ['*']
