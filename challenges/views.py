from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

weekly_challenges = {
    "monday": "Prepare food for the whole week!",
    "tuesday": "Do not eat meat all day!",
    "wednesday": "Go for a morning run!",
    "thursday": "Don't eat sweets all day!",
    "friday": "Go through 20 videos on the Django course!",
    "saturday": "Take 20,000 steps per day!",
    "sunday": None
}

# Create your views here.

def index(request):
    weeks = list(weekly_challenges.keys())

    return render(request, "challenges/index.html", {
        "weeks": weeks
    })

def weekly_challenge_by_number(request, week):
    weeks = list(weekly_challenges.keys())

    if week > len(weeks):
        return HttpResponseNotFound("Invalid week")

    redirect_week = weeks[week - 1]
    redirect_path = reverse("week-challenge", args=[redirect_week]) # /challenge/monday
    return HttpResponseRedirect(redirect_path)

def weekly_challenge(request, week):  
    try:
        challenge_text = weekly_challenges[week]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "week_name": week.capitalize()
        })
    except:
        raise Http404()