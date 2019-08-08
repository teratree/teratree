from django.urls import path

from . import views

app_name = 'experiment'
urlpatterns = [
    path('', views.home, name='experiment-home'),
]
