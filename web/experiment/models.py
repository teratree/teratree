import datetime

from django.conf import settings
from django.db import models
from django.utils import timezone

MAX_LENGTH=254


def two_weeks():
    return timezone.now() + datetime.timedelta(days=14)

NA = 'n/a'
LOW = 'low'
MEDIUM = 'medium'
HIGH = 'high'

IMPORTANCE_CHOICES = [
    (NA, 'N/A'),
    (LOW, 'Low'),
    (MEDIUM, 'Medium'),
    (HIGH, 'High'),
]

class Experiment(models.Model):
    poster = models.ForeignKey('Person', on_delete=models.PROTECT, related_name='posted_experiments', null=True, blank=True)
    posted = models.DateTimeField(default=timezone.now)

    hypothesis = models.TextField(blank=True, default='')
    experiment = models.TextField(blank=True, default='')
    measurement = models.TextField(blank=True, default='')

    importance = models.CharField(max_length=6, choices=IMPORTANCE_CHOICES, default=NA)
    cost = models.CharField(max_length=6, choices=IMPORTANCE_CHOICES, default=NA)
    time_required = models.CharField(max_length=6, choices=IMPORTANCE_CHOICES, default=NA)
    data_reliability = models.CharField(max_length=6, choices=IMPORTANCE_CHOICES, default=NA)
    action_required = models.CharField(max_length=6, choices=IMPORTANCE_CHOICES, default=NA)

    observation = models.TextField(blank=True, default='')
    learning = models.TextField(blank=True, default='')
    action = models.TextField(blank=True, default='')

    parents = models.ManyToManyField('Experiment', related_name='children', blank=True)

    def __str__(self):
        return f'Experiment {self.hypothesis}'

class ExperimentComment(models.Model):
    experiment = models.ForeignKey('Experiment', on_delete=models.CASCADE)
    comment = models.TextField(blank=True, default='')
    poster = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True, related_name='posted_experiment_comments')
    posted = models.DateTimeField(default=timezone.now)

# class ExperimentParent(models.Model):
#     parent_experiment = models.ForeignKey('Experiment', related_name='children', on_delete=models.CASCADE)
#     child_experiment = models.ForeignKey('Experiment', related_name='parents', on_delete=models.CASCADE)

class ExperimentRelatedExperience(models.Model):
    experiment = models.ForeignKey('Experiment', related_name='related_experiences', on_delete=models.CASCADE)
    experience = models.ForeignKey('Experience', related_name='related_experiments', on_delete=models.CASCADE)


class Person(models.Model):
    greeting_name = models.CharField(blank=True, default='', max_length=MAX_LENGTH)
    last_name = models.CharField(blank=True, default='', max_length=MAX_LENGTH)
    email = models.EmailField(blank=True, default='', max_length=MAX_LENGTH)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        s = f'{self.greeting_name}'
        if self.email:
            s += f' <{self.email}>'
        if self.username:
            s += f' ({self.username})'
        return s

    class Meta:
        verbose_name_plural='people'

class Experience(models.Model):
    experience = models.TextField(blank=True, default='')
    poster = models.ForeignKey('Person', on_delete=models.PROTECT, related_name='posted_experiences', null=True, blank=True)
    posted = models.DateTimeField(default=timezone.now)

    def snippet(self):
        return self.experience[0:60] + '...'

    def __str__(self):
        return f'{self.posted} {self.snippet()}'

class ExperienceComment(models.Model):
    experience = models.ForeignKey('Experience', on_delete=models.CASCADE)
    comment = models.TextField(blank=True, default='')
    poster = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True, related_name='posted_experience_comments')
    posted = models.DateTimeField(default=timezone.now)

