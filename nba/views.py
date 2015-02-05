from django.shortcuts import render

def nbahome(request):
    return render(request, 'nba/nbahome.html')
