from django.urls import path
from .views import homePage

app_name = 'SoundboxApp'

urlpatterns = [
    path('', homePage, name="home_page"),
]
