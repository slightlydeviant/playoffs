from django.shortcuts import render
from ncaaf.forms import MakeLeague
from django.views.generic import View

def ncaafhome(request):
    form = MakeLeague();
    return render(request, 'ncaaf/ncaafhome.html', { 'form': form })

class ncaafHome(View):
    """
    Class of functions handling NCAAF home page.

    """
    def get(self, request):
        form = MakeLeague()
        return render(request, 'ncaaf/ncaafhome.html', {'form': form})

    def post(self, request):
        form = MakeLeague(request.POST)
        if form.is_valid():
            # create league in code
            league = { 'id': 101011,
                       'name': form.cleaned_data['leaguename'],
                       'pw': form.cleaned_data['password'] }
            return render(request, 'ncaaf/ncaafhome.html', {'form': MakeLeague(), 'league': league})
        else:
            form = MakeLeague(form.cleaned_data)
            return render(request, 'ncaaf/ncaafhome.html', {'form': form})
