from allauth.account.forms import SignupForm as AllAuthSignUpForm
from experiment.models import MAX_LENGTH
from teratree.models import Profile
from django import forms


class SignUpForm(AllAuthSignUpForm):
    # Without required=False, the elements get an HTML required attribute so it 
    # shouldn't be possilbe to trigger the clean() method unless the browser is
    # bypassed. I think this is a nice behaviour.
    first_name = forms.CharField(max_length=MAX_LENGTH, label='First name') # , required=False)
    last_name = forms.CharField(max_length=MAX_LENGTH, label='Last name') # , required=False)

    agree_to_website_terms = forms.BooleanField(initial=False) #, required=False)
    opt_in_to_newsletter = forms.BooleanField(initial=False) #, required=False)

    def __init__(self, *k, **p):
        super().__init__(*k, **p)
        for name in ['first_name', 'last_name']:
            self.fields[name].widget.attrs['placeholder'] = self.fields[name].label

    def clean(self):
        super().clean()
        if not self.cleaned_data.get('first_name'):
           raise forms.ValidationError("Please enter a first name")
        if not self.cleaned_data.get('last_name'):
           raise forms.ValidationError("Please enter a last name")
        if not self.cleaned_data.get('agree_to_website_terms', False):
           raise forms.ValidationError("Please agree to the terms and conditions")

    def save(self, request):
        # .save() returns a User object, it already saves first_name and last_name
        user = super().save(request)
        # Add your own processing here.
        Profile.objects.create(agree_to_website_terms = self.cleaned_data['agree_to_website_terms'], user=user, opt_in_to_newsletter = self.cleaned_data['opt_in_to_newsletter'])
        # You must return the original result.
        return user
