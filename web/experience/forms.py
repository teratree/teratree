# from django.forms import ModelForm
# from .models import ExperiencePage
# 
# class ExperienceForm(ModelForm):
#     class Meta:
#         model = ExperiencePage
#         exclude = ('posted',)
#         fields = ('name', 'email', 'user', 'posted','experience')
# 
#     name = models.CharField(blank=True, default='', max_length=MAX_LENGTH)
#     email = models.EmailField(blank=True, default='', max_length=MAX_LENGTH)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='experience_pages')
#     posted = models.DateTimeField(default=timezone.now)
# 
#     experience = StreamField([
#         ('heading', blocks.CharBlock(classname="full title")),
#         ('paragraph', blocks.RichTextBlock()),
# 

from django import forms
from .models import ExperiencePageComment


class CommentForm(forms.ModelForm):

    def __init__(self, is_authenticated, *args, **kwargs):
        self.is_authenticated = is_authenticated
        super().__init__(*args, **kwargs)

    def clean(self):
        super().clean()
        if not self.is_authenticated:
           if not self.cleaned_data.get('name'):
               raise forms.ValidationError("Please enter a name or sign in")
           # if not self.cleaned_data.get('email'):
           #     raise forms.ValidationError("Please enter an email or sign in")

    class Meta:
        model = ExperiencePageComment
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'comment': 'Your Comment',
        }
        fields = ['name', 'email', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': labels['name']}),
            'email': forms.TextInput(attrs={'placeholder': labels['email']}),
            'comment': forms.Textarea(attrs={'placeholder': labels['comment']}),
        }
