from django.shortcuts import render
from .models import Music

# Create your views here
def homePage(request):
    music = Music.objects.all()
    context = {'music': music}
    return render(request, "home.html", context)