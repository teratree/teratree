import datetime

from django.conf import settings
from django.contrib import messages
from django.db import models
from django.shortcuts import render, redirect
from django.utils import timezone
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, StreamFieldPanel, TabbedInterface, ObjectList
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Orderable
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.search import index
from wagtailautocomplete.edit_handlers import AutocompletePanel
from blog.models import CommentsMixIn

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


# class Experiment(models.Model):
#     poster = models.ForeignKey('Person', on_delete=models.PROTECT, related_name='posted_experiments', null=True, blank=True)
#     posted = models.DateTimeField(default=timezone.now)
# 
#     hypothesis = models.TextField(blank=True, default='')
#     method = models.TextField(blank=True, default='')
#     measurement = models.TextField(blank=True, default='')
# 
#     importance = models.CharField(max_length=6, choices=IMPORTANCE_CHOICES, default=NA)
#     cost = models.CharField(max_length=6, choices=IMPORTANCE_CHOICES, default=NA)
#     time_required = models.CharField(max_length=6, choices=IMPORTANCE_CHOICES, default=NA)
#     data_reliability = models.CharField(max_length=6, choices=IMPORTANCE_CHOICES, default=NA)
#     action_required = models.CharField(max_length=6, choices=IMPORTANCE_CHOICES, default=NA)
# 
#     observation = models.TextField(blank=True, default='')
#     learning = models.TextField(blank=True, default='')
#     action = models.TextField(blank=True, default='')
# 
#     parents = models.ManyToManyField('Experiment', related_name='children', blank=True)
# 
#     def __str__(self):
#         return f'Experiment {self.hypothesis}'


class ExperimentPage(Page, CommentsMixIn):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='experiment_pages')
    posted = models.DateTimeField(default=timezone.now)

    hypothesis = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('document', DocumentChooserBlock()),
    ])

    method = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('document', DocumentChooserBlock()),
    ])

    measurement = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('document', DocumentChooserBlock()),
    ])


    importance = models.CharField(max_length=6, choices=IMPORTANCE_CHOICES, default=NA)
    cost = models.CharField(max_length=6, choices=IMPORTANCE_CHOICES, default=NA)
    time_required = models.CharField(max_length=6, choices=IMPORTANCE_CHOICES, default=NA)
    data_reliability = models.CharField(max_length=6, choices=IMPORTANCE_CHOICES, default=NA)
    action_required = models.CharField(max_length=6, choices=IMPORTANCE_CHOICES, default=NA)

    observation = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('document', DocumentChooserBlock()),
    ])

    learning = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('document', DocumentChooserBlock()),
    ])

    action = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('document', DocumentChooserBlock()),
    ])

    ranking_panels = [
        FieldPanel('importance'),
        FieldPanel('cost'),
        FieldPanel('time_required'),
        FieldPanel('data_reliability'),
        FieldPanel('action_required'),
    ]

    content_panels = Page.content_panels + [
        AutocompletePanel('user', target_model=settings.AUTH_USER_MODEL),
        FieldPanel('posted'),
        StreamFieldPanel('hypothesis'),
        StreamFieldPanel('method'),
        StreamFieldPanel('measurement'),
        StreamFieldPanel('observation'),
        StreamFieldPanel('learning'),
        StreamFieldPanel('action'),
        InlinePanel('comments', label="Comments"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('hypothesis'),
        index.SearchField('method'),
        index.SearchField('measurement'),
        index.SearchField('observation'),
        index.SearchField('learning'),
        index.SearchField('action'),
    ]

    subpage_types = [
        'experiment.ExperimentPage'
    ]

    # parent_page_types = [
    #     'experiment.ExperimentPage',
    #     'homepage.ContentPage',
    # ]


    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading='Content'),
            ObjectList(ranking_panels, heading="Ranking"),
            ObjectList(Page.promote_panels, heading='Promote'),
            ObjectList(Page.settings_panels, heading='Settings'),
        ]
    )


    def __str__(self):
        return f'Experiment Page {self.hypothesis}'

    def serve(self, request):    
        from .forms import CommentForm
        return self.add_comments_and_return(request, CommentForm)



class ExperimentPageComment(Orderable):
    page = ParentalKey(ExperimentPage, on_delete=models.CASCADE, related_name='comments')
    posted = models.DateTimeField(default=timezone.now)
    name = models.CharField(blank=True, max_length=250)
    email = models.EmailField(blank=True, default='', max_length=MAX_LENGTH)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='experiment_page_comments')
    comment = models.TextField(blank=True, max_length=1250)

    panels = [
        FieldPanel('name'),
        FieldPanel('email'),
        AutocompletePanel('user', target_model=settings.AUTH_USER_MODEL),
        FieldPanel('posted'),
        FieldPanel('comment'),
    ]

# class ExperimentComment(models.Model):
#     experiment = models.ForeignKey('Experiment', on_delete=models.CASCADE)
#     comment = models.TextField(blank=True, default='')
#     poster = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True, related_name='posted_experiment_comments')
#     posted = models.DateTimeField(default=timezone.now)
# 
# 
# class ExperimentRelatedExperience(models.Model):
#     experiment = models.ForeignKey('Experiment', related_name='related_experiences', on_delete=models.CASCADE)
#     experience = models.ForeignKey('Experience', related_name='related_experiments', on_delete=models.CASCADE)
# 
# 
# class Person(models.Model):
#     first_name = models.CharField(blank=True, default='', max_length=MAX_LENGTH)
#     last_name = models.CharField(blank=True, default='', max_length=MAX_LENGTH)
#     email = models.EmailField(blank=True, default='', max_length=MAX_LENGTH)
# 
#     autocomplete_search_field = 'email'
#     def autocomplete_label(self):
#         return self.email
# 
#     def __str__(self):
#         s = f'{self.first_name} {self.last_name}'
#         if self.email:
#             s += f' <{self.email}>'
#         return s
# 
#     class Meta:
#         verbose_name_plural='people'
# 
# 
# class Experience(models.Model):
#     experience = models.TextField(blank=True, default='')
#     poster = models.ForeignKey('Person', on_delete=models.PROTECT, related_name='posted_experiences', null=True, blank=True)
#     posted = models.DateTimeField(default=timezone.now)
# 
#     def snippet(self):
#         return self.experience[0:60] + '...'
# 
# 
# 
# class ExperienceComment(models.Model):
#     experience = models.ForeignKey('Experience', on_delete=models.CASCADE)
#     comment = models.TextField(blank=True, default='')
#     poster = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True, related_name='posted_experience_comments')
#     posted = models.DateTimeField(default=timezone.now)
# 
