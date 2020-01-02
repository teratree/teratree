from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.admin.edit_handlers import FieldPanel

class ContentPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class HomePage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('rawhtml', blocks.RawHTMLBlock()),
        ('document', DocumentChooserBlock()),
    ], blank=True)
    aside1 = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('rawhtml', blocks.RawHTMLBlock()),
        ('document', DocumentChooserBlock()),
    ],blank=True)
    aside2 = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('rawhtml', blocks.RawHTMLBlock()),
        ('document', DocumentChooserBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        StreamFieldPanel('aside1'),
        StreamFieldPanel('aside2'),
    ]


# See https://docs.djangoproject.com/en/dev/ref/templates/api/#compiling-a-string

from django.template import Context, Template
from django.http import HttpResponse

class TemplatePage(Page):
    template_content = models.TextField()
    region1 = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('rawhtml', blocks.RawHTMLBlock()),
        ('document', DocumentChooserBlock()),
    ], null=True, blank=True)
    region2 = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('rawhtml', blocks.RawHTMLBlock()),
        ('document', DocumentChooserBlock()),
    ], null=True, blank=True)
    region3 = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('rawhtml', blocks.RawHTMLBlock()),
        ('document', DocumentChooserBlock()),
    ], null=True, blank=True)
    region4 = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('rawhtml', blocks.RawHTMLBlock()),
        ('document', DocumentChooserBlock()),
    ], null=True, blank=True)
    region5 = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('rawhtml', blocks.RawHTMLBlock()),
        ('document', DocumentChooserBlock()),
    ], null=True, blank=True)
    region6 = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('rawhtml', blocks.RawHTMLBlock()),
        ('document', DocumentChooserBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('template_content', classname="full"),
        StreamFieldPanel('region1'),
        StreamFieldPanel('region2'),
        StreamFieldPanel('region3'),
        StreamFieldPanel('region4'),
        StreamFieldPanel('region5'),
        StreamFieldPanel('region6'),
    ]

    def serve(self, request):
        print('Got here')
        template = Template(self.template_content)
        context = Context({
            'page': self,
            'self': self,
            'request': request,
        })
        return HttpResponse(template.render(context))
