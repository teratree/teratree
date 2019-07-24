from .base import *


from djangosharedsettings.security import *
from djangosharedsettings.secret import *
from djangosharedsettings.bucket import *

DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
ALLOWED_HOSTS = [host.strip() for host in os.environ['ALLOWED_HOSTS'].split(',')]
PREPEND_WWW = True
