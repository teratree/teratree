from django.views.generic.edit import UpdateView
from .models import Profile
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin


class ProfileUpdate(SuccessMessageMixin, UpdateView):
    model = Profile
    fields = ['opt_in_to_newsletter']
    template_name_suffix = '_update_form'
    success_message = "Your settings were saved successfully"

    def get_success_url(self):
        return reverse('dashboard')

    def get_object(self):
        return self.request.user.profile.get()

class UserNameUpdate(SuccessMessageMixin, UpdateView):
    model = get_user_model()
    fields = ['first_name', 'last_name']
    template_name_suffix = '_update_form'
    success_message = "%(first_name)s %(last_name)s was updated successfully"

    def get_success_url(self):
        return reverse('dashboard')

    def get_object(self):
        return self.request.user

def dashboard(request):
    return render(request, 'teratree/dashboard.html')


def error500(request):
    raise Exception('Test Exception')
