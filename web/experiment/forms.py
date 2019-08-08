from django import forms
from .models import ExperimentPageComment


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
        model = ExperimentPageComment
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
