from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"), # /challenges
    path("<int:week>", views.weekly_challenge_by_number),
    path("<str:week>", views.weekly_challenge, name="week-challenge")
]