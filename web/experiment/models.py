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
    title = models.CharField(blank=False, unique=True, max_length=MAX_LENGTH)
    poster = models.ForeignKey('Person', on_delete=models.PROTECT, related_name='posted_experiments', null=True, blank=True)
    posted = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey('Person', on_delete=models.PROTECT, related_name='owned_experiments', null=True, blank=True)
    due = models.DateTimeField(default=two_weeks)
    hypothesis = models.TextField(blank=True, default='')
    importance = models.CharField(max_length=6, choices=IMPORTANCE_CHOICES, default=NA)
    experiment = models.TextField(blank=True, default='')
    cost = models.CharField(max_length=6, choices=IMPORTANCE_CHOICES, default=NA)
    data_reliability = models.CharField(max_length=6, choices=IMPORTANCE_CHOICES, default=NA)
    measurement = models.TextField(blank=True, default='')
    time_required = models.CharField(max_length=6, choices=IMPORTANCE_CHOICES, default=NA)
    condition = models.TextField(blank=True, default='')

    def __str__(self):
        return f'Experiment {self.title}'

class Learning(models.Model):
    title = models.CharField(blank=False, unique=True, max_length=MAX_LENGTH)
    poster = models.ForeignKey('Person', on_delete=models.PROTECT, related_name='posted_learnings', null=True, blank=True)
    posted = models.DateTimeField(default=timezone.now)
    # XXX Would like a date guestimate field
    occurred = models.DateTimeField(default=timezone.now)
    hypothesis = models.TextField(blank=True, default='')
    data_reliability = models.CharField(max_length=6, choices=IMPORTANCE_CHOICES, default=NA)
    observation = models.TextField(blank=True, default='')
    learning = models.TextField(blank=True, default='')
    action_required = models.CharField(max_length=6, choices=IMPORTANCE_CHOICES, default=NA)
    action = models.TextField(blank=True, default='')

class LearningComment(models.Model):
    experiment = models.ForeignKey('Learning', on_delete=models.CASCADE)
    comment = models.TextField(blank=True, default='')
    poster = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True, related_name='posted_learning_comments')
    posted = models.DateTimeField(default=timezone.now)

class ExperienceComment(models.Model):
    experiment = models.ForeignKey('Experience', on_delete=models.CASCADE)
    comment = models.TextField(blank=True, default='')
    poster = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True, related_name='posted_experience_comments')
    posted = models.DateTimeField(default=timezone.now)

class ExperimentComment(models.Model):
    experiment = models.ForeignKey('Experiment', on_delete=models.CASCADE)
    comment = models.TextField(blank=True, default='')
    poster = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True, related_name='posted_experiment_comments')
    posted = models.DateTimeField(default=timezone.now)

class LearningFromExperiment(models.Model):
    learning = models.ForeignKey('Learning', on_delete=models.PROTECT)
    experiment = models.ForeignKey('Experiment', on_delete=models.PROTECT)

class LearningFromExperience(models.Model):
    learning = models.ForeignKey('Learning', on_delete=models.PROTECT)
    experience = models.ForeignKey('Experience', on_delete=models.PROTECT)

class ExperimentBasedOnLearning(models.Model):
    experiment = models.ForeignKey('Experiment', on_delete=models.PROTECT)
    learning = models.ForeignKey('Learning', on_delete=models.PROTECT)

class ExperimentBasedOnExperience(models.Model):
    experiment = models.ForeignKey('Experiment', on_delete=models.PROTECT)
    experience = models.ForeignKey('Experience', on_delete=models.PROTECT)

class Person(models.Model):
    greeting_name = models.CharField(blank=True, default='', max_length=MAX_LENGTH)
    email = models.EmailField(blank=True, default='', max_length=MAX_LENGTH)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        s = f'{self.greeting_name}'
        if self.email:
            s += f' <{self.email}>'
        if self.username:
            s += f' ({self.username})'
        return s


class Experience(models.Model):
    experience = models.TextField(blank=True, default='')
    poster = models.ForeignKey('Person', on_delete=models.PROTECT, related_name='posted_experiences', null=True, blank=True)
    posted = models.DateTimeField(default=timezone.now)

    def snippet(self):
        return self.experience[0:60] + '...'

    def __str__(self):
        return f'{self.posted} {self.snippet()}'

class Results00001Data(models.Model):
    posted = models.DateTimeField(default=timezone.now)
    respondant = models.ForeignKey('Person', on_delete=models.PROTECT, related_name='response_to_000001', null=True, blank=True)
    location = models.CharField(max_length=MAX_LENGTH, default='', blank=True, help_text='Where did they answer?')
    question1 = models.TextField(blank=True, default='', help_text='When did you last plant a tree?')
    question2 = models.TextField(blank=True, default='', help_text='If I gave you a tree tomorrow what would you do with it?')
    question3 = models.TextField(blank=True, default='', help_text='How would you get a tree?')
    cczero = models.BooleanField(default=False, help_text='Can we put your name and answers online under a cczero license so others can use them?')
