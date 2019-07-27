'''
./manage.py startapp


and add it to INSTALLED_APPS

from django.urls import path, re_path, include

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls

urlpatterns = [
    ...
    re_path(r'^cms/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'^pages/', include(wagtail_urls)),
    ...
]


re_path(r'', include(wagtail_urls)),



from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



'''

from .base_08_allauth import *

# Based on http://docs.wagtail.io/en/v2.5.1/advanced_topics/settings.html
for middleware in [
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'django.middleware.security.SecurityMiddleware',

  'wagtail.core.middleware.SiteMiddleware',

  'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]:
    if middleware not in MIDDLEWARE:
        MIDDLEWARE.append(middleware)

for app in [
  'wagtail.contrib.forms',
  'wagtail.contrib.redirects',
  'wagtail.embeds',
  'wagtail.sites',
  'wagtail.users',
  'wagtail.snippets',
  'wagtail.documents',
  'wagtail.images',
  'wagtail.search',
  'wagtail.admin',
  'wagtail.core',

  'taggit',
  'modelcluster',

  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
]:
    if app not in INSTALLED_APPS:
        INSTALLED_APPS.append(app)

# Probably worth setting this to the same as Django's APPEND_SLASH
# https://docs.djangoproject.com/en/2.2/ref/settings/#append-slash
WAGTAIL_APPEND_SLASH = APPEND_SLASH = False


# To set up search follow: http://docs.wagtail.io/en/v2.5.1/advanced_topics/settings.html#search


# Based on http://docs.wagtail.io/en/v2.5.1/getting_started/integrating_into_django.html
for app in [
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    
    'modelcluster',
    'taggit',
]:
    if app not in INSTALLED_APPS:
        INSTALLED_APPS.append(app)

for middleware in [
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]:
    if middleware not in MIDDLEWARE:
        MIDDLEWARE.append(middleware)

# These aren't needed because they are set up in other settings files
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'


WAGTAIL_SITE_NAME = 'teratree'

