from django.shortcuts import render
from .models import Music

# Create your views here
def homePage(request):
    music = Music.objects.all()
    music_list=list(Music.objects.all().values())
    context = {'music': music, 'music_list': music_list}
    return render(request, "home.html", context)