from django.urls import path
from . import views

app_name = 'SoundboxApp'

urlpatterns = [
    path("", views.index, name="index"),
]
