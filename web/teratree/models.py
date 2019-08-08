from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


# This is to allow other Page-based models to lookup a user
# See https://wagtail-autocomplete.readthedocs.io/en/latest/customization.html
User = get_user_model()
def autocomplete_label(self):
    return self.email
User.autocomplete_search_field = 'email'
User.autocomplete_label = autocomplete_label


class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='profile')
    agree_to_website_terms = models.BooleanField(default=False)
    opt_in_to_newsletter = models.BooleanField(default=False)

    def __str__(self):
        return f'Profile for {self.user.username}'


from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel


class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
        FormSubmissionsPanel(),
    ]

