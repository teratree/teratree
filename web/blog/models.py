from django.db import models
import pytz

from django.conf import settings
from django.utils.timezone import now
from django.utils import timezone
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index
from wagtailautocomplete.edit_handlers import AutocompletePanel

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        # print(self.get_children())
        # print(self.get_children()[0])
        # print(dir(self.get_children()[0]))
        blogpages = BlogPage.objects.child_of(self).order_by('-date').live()
        # self.get_children().filter(date__gt=timezone.now()).order_by('-date').live() #.order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context


from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.admin.edit_handlers import InlinePanel
from wagtail.images.blocks import ImageChooserBlock
import datetime
from django.shortcuts import render, redirect


from django.contrib import messages

class CommentsMixIn:
    def add_comments_and_return(self, request, CommentForm):
        if request.method == 'POST':
            form = CommentForm(request.user.is_authenticated, request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.date = now().astimezone(pytz.UTC)
                comment.sort_order = self.comments.all().count()
                if request.user.is_authenticated:
                    comment.user = request.user
                self.comments.add(comment)
                comment.save()
                messages.success(request, 'Commented added successfully.')
                return redirect(self.url)
        else:
            form = CommentForm(request.user.is_authenticated)

        return render(request, self.template, {
            'page': self,
            'self': self,
            'form': form,
            'request': request,
        })




from django.db import models

# New imports added for ParentalKey, Orderable, InlinePanel, ImageChooserPanel
class BlogPage(Page, CommentsMixIn):
    date = models.DateField("Post date")
    time = models.TimeField("Post time")
    intro = models.CharField(max_length=1250)
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('rawhtml', blocks.RawHTMLBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('time'),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
        InlinePanel('comments', label="Comments"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]


    subpage_types = [
        'blog.BlogIndexPage'
    ]


    def serve(self, request):    
        from .forms import CommentForm
        return self.add_comments_and_return(request, CommentForm)


from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


from django.db import models
from django.conf import settings



class BlogPageComment(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='comments')
    posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='blog_page_comments')
    name = models.CharField(blank=True, max_length=250)
    email = models.EmailField(blank=True, max_length=250)
    comment = models.TextField(blank=True, max_length=1250)

    panels = [
        FieldPanel('name'),
        FieldPanel('email'),
        AutocompletePanel('user', target_model=settings.AUTH_USER_MODEL),
        FieldPanel('posted'),
        FieldPanel('comment'),
    ]
