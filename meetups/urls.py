from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="all-meetups"),
    path(
        "<slug:meetup_slug>/confirmation",
        views.confirmation,
        name="confirmation",
    ),
    path("<slug:meetup_slug>/", views.meetup_details, name="meetup-detail"),
]
