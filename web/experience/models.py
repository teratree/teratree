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

from django.conf import settings


class ExperiencePage(Page, CommentsMixIn):
    name = models.CharField(blank=True, default='', max_length=MAX_LENGTH)
    email = models.EmailField(blank=True, default='', max_length=MAX_LENGTH)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='experience_pages')
    posted = models.DateTimeField(default=timezone.now)

    experience = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('document', DocumentChooserBlock()),
    ])

    importance = models.CharField(max_length=6, choices=IMPORTANCE_CHOICES, default=NA)
    data_reliability = models.CharField(max_length=6, choices=IMPORTANCE_CHOICES, default=NA)
    action = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('document', DocumentChooserBlock()),
    ], blank=True)

    ranking_panels = [
        FieldPanel('importance'),
        FieldPanel('data_reliability'),
        StreamFieldPanel('action'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('email'),
        AutocompletePanel('user', target_model=settings.AUTH_USER_MODEL),
        FieldPanel('posted'),
        StreamFieldPanel('experience'),
        InlinePanel('comments', label="Comments"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('experience'),
    ]

    subpage_types = [
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
        return f'Experience Page {self.slug}'

    def serve(self, request):    
        from .forms import CommentForm
        return self.add_comments_and_return(request, CommentForm)


class ExperiencePageComment(Orderable):
    page = ParentalKey(ExperiencePage, on_delete=models.CASCADE, related_name='comments')
    posted = models.DateTimeField(default=timezone.now)
    name = models.CharField(blank=True, max_length=250)
    email = models.EmailField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='experience_page_comments')
    comment = models.TextField(blank=True, max_length=1250)

    panels = [
        FieldPanel('name'),
        FieldPanel('email'),
        AutocompletePanel('user', target_model=settings.AUTH_USER_MODEL),
        FieldPanel('posted'),
        FieldPanel('comment'),
    ]
