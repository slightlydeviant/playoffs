from django.shortcuts import render

def ncaamhome(request):
    return render(request, 'ncaam/ncaamhome.html')
