from __future__ import unicode_literals
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms.util import ErrorList
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


class LogInForm(forms.Form):
    """
    Form that controls log in attributes.

    """
    username = forms.CharField(label='Username', max_length=50,
        error_messages={'required': 'Enter a valid username'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput,
        error_messages={'required': 'This field is required'})

    def clean_username(self):
        """
        Validate that the username exists.

        """
        existing = User.objects.filter(username__exact=self.cleaned_data['username'])
        if existing.exists():
            return self.cleaned_data['username']
        else:
            raise forms.ValidationError(_("A user with that username does not exist."))

    def __init__(self, *args, **kwargs):
        super(LogInForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].widget.attrs['autofocus'] = 'autofocus'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.helper = FormHelper()
        self.helper.form_id = 'id-logInForm'
        self.helper.form_class = 'crisp'
        self.helper.form_method = 'post'
        self.helper.form_action = 'login'
        self.helper.add_input(Submit('submit', 'Log-in'))

class RegistrationForm(forms.Form):
    """
    Form for registering a new user account. (Adapted from django-registration)

    Validates that the requested username is not already in use,
    that the requested email is not already in use, and
    requires the password to be entered twice to catch typos.

    """
    required_css_class = 'required'

    first_name = forms.CharField(label=_("First Name"))
    last_name = forms.CharField(label=_("Last Name"))
    username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                max_length=30,
                                label=_("Username"),
                                error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})
    email = forms.EmailField(label=_("E-mail"))
    password1 = forms.CharField(widget=forms.PasswordInput,
                                label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label=_("Password (again)"),
                                error_messages={'required': _("Passwords did not match")})

    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match, and that the username and email are unique.
        Note that an error here will end up in ``non_field_errors()``
        because it doesn't apply to a single field.

        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields didn't match."))

        if 'username' in self.cleaned_data:
            existing = User.objects.filter(username__exact=self.cleaned_data['username'])
            if existing.exists():
                self._errors['username'] = ErrorList([u"Enter a different username"])
                raise forms.ValidationError(_("A user with that username already exists."))

        if 'email' in self.cleaned_data:
            if User.objects.filter(email__iexact=self.cleaned_data['email']):
                self._errors['email'] = ErrorList([u"This email address is already in use"])
                raise forms.ValidationError(_("This email address is already in use. Please supply a different email address, or try recovering your password."))

        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].widget.attrs['autofocus'] = 'autofocus'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password (again)'
        self.helper = FormHelper()
        self.helper.form_id = 'id-RegistrationForm'
        self.helper.form_class = 'crisp'
        self.helper.form_method = 'post'
        self.helper.form_action = 'register'
        self.helper.add_input(Submit('submit', 'Register'))

class MyPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(MyPasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].widget.attrs['autofocus'] = 'autofocus'
        self.helper = FormHelper()
        self.helper.form_id = 'id-PasswordResetForm'
        self.helper.form_class = 'crisp'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'Reset'))

class MySetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(MySetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'
        self.fields['new_password1'].widget.attrs['autofocus'] = 'autofocus'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'New Password (again)'
        self.helper = FormHelper()
        self.helper.form_id = 'id-PasswordResetForm'
        self.helper.form_class = 'crisp'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'Change Password'))
