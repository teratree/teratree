
from django import forms
from .models import BlogPageComment


class CommentForm(forms.ModelForm):
    comment = forms.CharField( widget=forms.Textarea, label="Your Comment")
    class Meta:
        model = BlogPageComment
        fields = ['author', 'comment']
        labels = {
            'author': 'Your Name',
            'comment': 'Your Comment',
        }
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': labels['author']}),
            'comment': forms.Textarea(attrs={'placeholder': labels['comment']}),
        }

