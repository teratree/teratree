"""teratree URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.urls import path, re_path, include

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls

from django.views.generic.base import RedirectView
from wagtailautocomplete.urls.admin import urlpatterns as autocomplete_admin_urls


from .views import ProfileUpdate, UserNameUpdate, dashboard, error500


app_name = 'teratree'
urlpatterns = [
    # path('_internal/404', error404),
    path('_internal/500', error500),
    path('dashboard/name', UserNameUpdate.as_view(), name='dashboard-name'),
    path('dashboard/profile', ProfileUpdate.as_view(), name='dashboard-profile'),
    path('dashboard', dashboard, name='dashboard'),
    path('admin/autocomplete/', include(autocomplete_admin_urls)),
    # Instead, follow this pattern
    # path('experience/', include('experience.urls')),
    # path('data/', include('data.urls')),
    # path('experiment/', include('experiment.urls')),
    # This is how wagtail recommends it is done, don't copy this
    re_path(r'^documents/', include(wagtaildocs_urls)),
    path('cms/login/', RedirectView.as_view(url='/accounts/login', query_string=True, permanent=False), name='index'),
    re_path(r'^cms/', include(wagtailadmin_urls)),
    path('_util/login/', RedirectView.as_view(url='/accounts/login', query_string=True, permanent=False), name='index'),
    path('admin/login/', RedirectView.as_view(url='/accounts/login', query_string=True, permanent=False), name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # Put this after accounts above to use the AllAuth URLs by default
    re_path(r'^', include(wagtail_urls)),
]

from django.conf import settings

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
