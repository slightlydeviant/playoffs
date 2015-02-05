from django.shortcuts import render

def ncaawhome(request):
    return render(request, 'ncaaw/ncaawhome.html')
