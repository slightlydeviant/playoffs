from django.shortcuts import render

def nflhome(request):
    return render(request, 'nfl/nflhome.html')
