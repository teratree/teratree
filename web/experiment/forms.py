from django.forms import ModelForm
from .models import Experience

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        exclude = ('posted',)

