from django.urls import path
from .views import homePage, addMusic

app_name = 'SoundboxApp'

urlpatterns = [
    path('', homePage, name="home_page"),
    path('add/', addMusic, name="add_music"),
]
