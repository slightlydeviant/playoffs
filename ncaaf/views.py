from django.shortcuts import render

def ncaafhome(request):
    return render(request, 'ncaaf/ncaafhome.html')
