from SoundboxApp.form import AddMusicForm
from django.shortcuts import render
from .models import Music, Album

# Create your views here
def homePage(request):
    music = Music.objects.all()
    music_list=list(Music.objects.all().values())
    context = {'music': music, 'music_list': music_list}
    return render(request, "home.html", context)


def addMusic(request):
    form=AddMusicForm()
    if request.POST:
        form=AddMusicForm(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            album=form.cleaned_data.get('album')
            if album:
                music_album=Album.object.get_or_create(name=album)
                instance.album=music_album[0]
                instance.save()
            else:
                instance.save()
            return redirect("music:home_page")
    context = {'form': form}
    return render(request, "addPage.html", context)