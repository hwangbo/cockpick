from django.shortcuts import render

# Create your views here.

def cockpick(request):
    return render(request, 'home.html')