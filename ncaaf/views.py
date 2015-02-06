from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from ncaaf.forms import MakeLeague
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
    try:
        league = League.objects.get(pk=leagueId)
    except League.DoesNotExist:
        raise Http404("League does not exist")
    return render(request, 'ncaaf/leaguehome.html', { 'league': league })
    # return HttpResponse("You're looking at league %s." % leagueId)
