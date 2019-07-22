from django.urls import path

from . import views

app_name = 'experiment'
urlpatterns = [
    path('', views.home, name='home'),
    path('experience/<int:experience_id>/', views.experience_detail, name='experience-detail'),
    path('experience/', views.experience_index, name='experience-index'),
    path('experience/create', views.experience_create, name='experience-create'),
]
