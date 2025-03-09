from django.shortcuts import render, redirect

from .forms import RegistrationForm
from .models import Meetup, Participant


# Create your views here.


def index(request):
    meetups = Meetup.objects.all()
    return render(request, "meetups/index.html", {"meetups": meetups})


def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == "GET":
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data["email"]
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect("confirmation", meetup_slug=meetup_slug)
        return render(
            request,
            "meetups/meetup-details.html",
            {
                "meetup": selected_meetup,
                "meetup_found": True,
                "registration_form": registration_form,
            },
        )
    except Exception as exc:
        print(exc)
        return render(request, "meetups/meetup-details.html", {"meetup_found": False})


def confirmation(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(
        request,
        "meetups/confirmation.html",
        {"organizer_email": meetup.organizer_email},
    )
