from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.apps import apps

MAX_LENGTH=254


class Questions00001(models.Model):
    posted = models.DateTimeField(default=timezone.now)

    first_name = models.CharField(blank=True, default='', max_length=MAX_LENGTH)
    last_name = models.CharField(blank=True, default='', max_length=MAX_LENGTH)
    email = models.EmailField(blank=True, default='', max_length=MAX_LENGTH)


    location = models.CharField(max_length=MAX_LENGTH, default='', blank=True, help_text='Where did they answer?')
    question1 = models.TextField(blank=True, default='', help_text='When did you last plant a tree?')
    question2 = models.TextField(blank=True, default='', help_text='If I gave you a tree tomorrow what would you do with it?')
    question3 = models.TextField(blank=True, default='', help_text='How would you get a tree?')
    cczero = models.BooleanField(default=False, help_text='Can we put your name and answers online under a cczero license so others can use them?')

    class Meta:
        verbose_name_plural='questions00001'
