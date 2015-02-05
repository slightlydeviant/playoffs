from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from accounts.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

class LogIn(View):
    """
    Class of functions handling user log in.

    """
    def get(self, request):
        logout(request)
        form = LogInForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = LogInForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'],
                                password = form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                error = "1"
                return render(request, 'accounts/login.html', {'form': form, 'error': error})
        else:
            form = LogInForm(form.cleaned_data)
            error = "2"
            return render(request, 'accounts/login.html', {'form': form, 'error': error})

class RegisterUser(View):
    """
    Class of functions handling user registration.

    """
    def get(self, request):
        logout(request)
        form = RegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username = form.cleaned_data['username'],
                                            password = form.cleaned_data['password1'],
                                            first_name = form.cleaned_data['first_name'],
                                            last_name = form.cleaned_data['last_name'],
                                            email = form.cleaned_data['email'])
            user.save()
            user_login = authenticate(username = form.cleaned_data['username'],
                                      password = form.cleaned_data['password1'])
            login(request, user_login)
            return HttpResponseRedirect(reverse('home'))
        else:
            form = RegistrationForm(form.cleaned_data)
            return render(request, 'accounts/register.html', {'form': form})

def LogOut(request):
    """
    Log out current user.

    """
    logout(request)
    return HttpResponseRedirect(reverse('home'))
