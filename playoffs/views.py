from django.shortcuts import render, get_object_or_404, render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from playoffs.search_functions import normalize_query, get_query
from ncaaf.models import League

def home(request):
    return render(request, 'home.html')

def search(request):
    """
    From http://julienphalip.com/post/2825034077/adding-search-to-a-django-site-in-a-snap
    Handles the nav bar search functionality.

    """
    query_string = ''
    found_entries = None
    found_ids = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        entry_query = get_query(query_string, ['leagueName',])
        found_entries = League.objects.filter(entry_query).order_by('id')

        id_query = get_query(query_string, ['id',])
        found_ids = League.objects.filter(id_query)

        leagues = League.objects.filter(leagueusers__userId=request.user.id)

    return render_to_response('searchresults.html',
                              { 'query_string': query_string, 'found_entries': found_entries, 'found_ids': found_ids, 'user_leagues': leagues },
                              context_instance=RequestContext(request))
