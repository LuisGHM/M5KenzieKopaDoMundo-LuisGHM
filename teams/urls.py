from django.urls import path
from .views import teamsView, teamsIdView


urlpatterns = [
    path("teams/", teamsView.as_view()),
    path("teams/<int:team_id>/", teamsIdView.as_view())
]