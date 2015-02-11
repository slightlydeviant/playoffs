from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from ncaaf.forms import MakeLeague, JoinPrivateLeague
from ncaaf.models import *
from django.contrib.auth.models import User
from django.views.generic import View

def ncaafhome(request):
    form = MakeLeague();
    return render(request, 'ncaaf/ncaafhome.html', { 'form': form })

class ncaafHome(View):
    """
    Class of functions handling NCAAF home page.

    """
    def get(self, request):
        if request.user.is_authenticated():
            form = MakeLeague()
            return render(request, 'ncaaf/ncaafhome.html', {'form': form})
        else:
            return render(request, 'ncaaf/ncaafhome.html')


    def post(self, request):
        form = MakeLeague(request.POST)
        if form.is_valid():
            # create league in code
            league = League(leagueName = form.cleaned_data['leaguename'],
                            ruleFormat = Rules.objects.get(pk=1),
                            isPrivate = form.cleaned_data['privacy'],
                            password = form.cleaned_data['password'],
                            creator = request.user,
                            sportId = Sports.objects.get(sportName='ncaaf'))
            league.save()
            leagueuser = LeagueUsers(leagueId = League.objects.get(pk=league.id),
                                     userId = request.user)
            leagueuser.save()
            # parse email textarea and send invites
            return render(request, 'ncaaf/ncaafhome.html', {'form': MakeLeague(), 'league': league})
        else:
            form = MakeLeague(form.cleaned_data)
            return render(request, 'ncaaf/ncaafhome.html', {'form': form})

def leaguehome(request, leagueId):
    """
    View creating the League Home page. You must be logged in to view a league.
    If, once you log in, the league is private and you are not part of it,
    display a javascript pop up asking for league password before rendering ANY of
    the page.

    """
    if not request.user.is_authenticated():
        return redirect('/accounts/login/?next=%s' % request.path)
    else:
        try:
            league = League.objects.get(pk=leagueId)
        except League.DoesNotExist:
            raise Http404("League does not exist")
        return render(request, 'ncaaf/leaguehome.html', { 'league': league })

class leaguejoin(View):
    """
    View controlling league joining logic. Includes private league password entry
    and checks to make sure a user is not already in that league.

    """
    def get(self, request, leagueId):
        if not request.user.is_authenticated():
            return redirect('/accounts/login/?next=%s' % request.path)
        else:
            try:
                league = League.objects.get(pk=leagueId)
            except League.DoesNotExist:
                raise Http404("League does not exist")
            # Automatically join and redirect to league home if public
            if league.isPrivate == False:
                if request.user.id in league.leagueusers_set.values_list('userId', flat=True):
                    return render(request, 'ncaaf/leaguehome.html', { 'league': league })
                else:
                    lu = LeagueUsers(userId = request.user, leagueId = league)
                    lu.save()
                    return render(request, 'ncaaf/leaguehome.html', { 'league': league })
            # Bring up private join page if private
            else:
                form = JoinPrivateLeague();
                return render(request, 'ncaaf/leaguejoin.html', { 'league': league, 'form': form })

    def post(self, request, leagueId):
        form = JoinPrivateLeague(request.POST)
        try:
            league = League.objects.get(pk=leagueId)
        except League.DoesNotExist:
            raise Http404("League does not exist")
        if form.is_valid():
            if form.cleaned_data['password'] == league.password:
                lu = LeagueUsers(userId = request.user, leagueId = league)
                lu.save()
                return render(request, 'ncaaf/leaguehome.html', { 'league': league })
            else:
                error = "The entered password did not match League password"
                form = JoinPrivateLeague(form.cleaned_data)
                return render(request, 'ncaaf/leaguejoin.html', { 'league': league, 'form': form, 'error': error })
        else:
            form = JoinPrivateLeague(form.cleaned_data)
            return render(request, 'ncaaf/leaguejoin.html', { 'league': league, 'form': form })
