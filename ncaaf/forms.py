from __future__ import unicode_literals
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms.util import ErrorList
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


class MakeLeague(forms.Form):
    """
    Form that creates a new league.

    """
    leaguename = forms.CharField(label='League Name', max_length=100,
        error_messages={'required': 'Enter a valid league name'})
    privacy = forms.BooleanField(label='Check if this is a Private league',
        required=False)
    password = forms.CharField(label='Password to join league',
        required=False)
    invitees = forms.CharField(label="Enter email addresses of people you'd like to invite to this league (separated by spaces, semicolons or commas)",
        required=False, widget=forms.Textarea)

    def clean(self):
        """
        Verifiy that there is a password if privacy has been checked

        """
        if 'privacy' in self.cleaned_data:
            if self.cleaned_data['privacy'] is True:
                if self.cleaned_data['password'] is "":
                    raise forms.ValidationError(_("A private league must have a password"))

        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(MakeLeague, self).__init__(*args, **kwargs)
        self.fields['leaguename'].widget.attrs['placeholder'] = 'League Name'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.helper = FormHelper()
        self.helper.form_id = 'id-ncaafLeagueForm'
        self.helper.form_class = 'crisp'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'Create'))
