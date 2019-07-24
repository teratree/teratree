from .base import *

if 'django.contrib.sites' not in INSTALLED_APPS:
    INSTALLED_APPS.append('django.contrib.sites')
if 'django.template.context_processors.request' not in TEMPLATES[0]['OPTIONS']['context_processors']:
    TEMPLATES[0]['OPTIONS']['context_processors'].append('django.template.context_processors.request')

if 'AUTHENTICATION_BACKENDS' not in locals():
    AUTHENTICATION_BACKENDS = []
if 'django.contrib.auth.backends.ModelBackend' not in AUTHENTICATION_BACKENDS:
    AUTHENTICATION_BACKENDS.append('django.contrib.auth.backends.ModelBackend')
if 'allauth.account.auth_backends.AuthenticationBackend' not in AUTHENTICATION_BACKENDS:
    AUTHENTICATION_BACKENDS.append('allauth.account.auth_backends.AuthenticationBackend')
for app in [
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]:
    if app not in INSTALLED_APPS:
        INSTALLED_APPS.append(app)
for app in [
    # ... include the providers you want to enable:
    # 'allauth.socialaccount.providers.agave',
    # 'allauth.socialaccount.providers.amazon',
    # 'allauth.socialaccount.providers.angellist',
    # 'allauth.socialaccount.providers.asana',
    # 'allauth.socialaccount.providers.auth0',
    # 'allauth.socialaccount.providers.authentiq',
    # 'allauth.socialaccount.providers.baidu',
    # 'allauth.socialaccount.providers.basecamp',
    # 'allauth.socialaccount.providers.bitbucket',
    # 'allauth.socialaccount.providers.bitbucket_oauth2',
    # 'allauth.socialaccount.providers.bitly',
    # 'allauth.socialaccount.providers.cern',
    # 'allauth.socialaccount.providers.coinbase',
    # 'allauth.socialaccount.providers.dataporten',
    # 'allauth.socialaccount.providers.daum',
    # 'allauth.socialaccount.providers.digitalocean',
    # 'allauth.socialaccount.providers.discord',
    # 'allauth.socialaccount.providers.disqus',
    # 'allauth.socialaccount.providers.douban',
    # 'allauth.socialaccount.providers.draugiem',
    # 'allauth.socialaccount.providers.dropbox',
    # 'allauth.socialaccount.providers.dwolla',
    # 'allauth.socialaccount.providers.edmodo',
    # 'allauth.socialaccount.providers.eveonline',
    # 'allauth.socialaccount.providers.evernote',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.feedly',
    # 'allauth.socialaccount.providers.fivehundredpx',
    # 'allauth.socialaccount.providers.flickr',
    # 'allauth.socialaccount.providers.foursquare',
    # 'allauth.socialaccount.providers.fxa',
    # 'allauth.socialaccount.providers.github',
    # 'allauth.socialaccount.providers.gitlab',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.hubic',
    # 'allauth.socialaccount.providers.instagram',
    # 'allauth.socialaccount.providers.jupyterhub',
    # 'allauth.socialaccount.providers.kakao',
    # 'allauth.socialaccount.providers.line',
    # 'allauth.socialaccount.providers.linkedin',
    # 'allauth.socialaccount.providers.linkedin_oauth2',
    # 'allauth.socialaccount.providers.mailru',
    # 'allauth.socialaccount.providers.mailchimp',
    # 'allauth.socialaccount.providers.meetup',
    # 'allauth.socialaccount.providers.microsoft',
    # 'allauth.socialaccount.providers.naver',
    # 'allauth.socialaccount.providers.nextcloud',
    # 'allauth.socialaccount.providers.odnoklassniki',
    # 'allauth.socialaccount.providers.openid',
    # 'allauth.socialaccount.providers.openstreetmap',
    # 'allauth.socialaccount.providers.orcid',
    # 'allauth.socialaccount.providers.paypal',
    # 'allauth.socialaccount.providers.patreon',
    # 'allauth.socialaccount.providers.persona',
    # 'allauth.socialaccount.providers.pinterest',
    # 'allauth.socialaccount.providers.reddit',
    # 'allauth.socialaccount.providers.robinhood',
    # 'allauth.socialaccount.providers.sharefile',
    # 'allauth.socialaccount.providers.shopify',
    # 'allauth.socialaccount.providers.slack',
    # 'allauth.socialaccount.providers.soundcloud',
    # 'allauth.socialaccount.providers.spotify',
    # 'allauth.socialaccount.providers.stackexchange',
    # 'allauth.socialaccount.providers.steam',
    # 'allauth.socialaccount.providers.strava',
    # 'allauth.socialaccount.providers.stripe',
    # 'allauth.socialaccount.providers.trello',
    # 'allauth.socialaccount.providers.tumblr',
    # 'allauth.socialaccount.providers.twentythreeandme',
    # 'allauth.socialaccount.providers.twitch',
    # 'allauth.socialaccount.providers.twitter',
    # 'allauth.socialaccount.providers.untappd',
    # 'allauth.socialaccount.providers.vimeo',
    # 'allauth.socialaccount.providers.vimeo_oauth2',
    # 'allauth.socialaccount.providers.vk',
    # 'allauth.socialaccount.providers.weibo',
    # 'allauth.socialaccount.providers.weixin',
    # 'allauth.socialaccount.providers.windowslive',
    # 'allauth.socialaccount.providers.xing',
]:
    if app not in INSTALLED_APPS:
        INSTALLED_APPS.append(app)


SITE_ID = 1


'''
urls.py:

urlpatterns = [
    ...
    url(r'^accounts/', include('allauth.urls')),
    ...
]
Note that you do not necessarily need the URLs provided by django.contrib.auth.urls. Instead of the URLs login, logout, and password_change (among others), you can use the URLs provided by allauth: account_login, account_logout, account_set_password…

Add a Site for your domain, matching settings.SITE_ID (django.contrib.sites app).
For each OAuth based provider, add a Social App (socialaccount app).
Fill in the site and the OAuth app credentials obtained from the provider.
''' 


# Don't require users to confirm their emails again when they click on a link
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# Choose a real URL:
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_PRESERVE_USERNAME_CASING = False
ACCOUNT_EMAIL_SUBJECT_PREFIX = ''
if not DEBUG:
    ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_SESSION_REMEMBER = False
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = False

SOCIALACCOUNT_STORE_TOKENS = False

ACCOUNT_USER_DISPLAY = lambda user: user.email

ACCOUNT_LOGOUT_ON_GET = True
