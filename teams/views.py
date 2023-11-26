from rest_framework.views import APIView, Request, Response, status
from teams.models import Team
from django.db import IntegrityError
from django.forms import model_to_dict
from utils import data_processing
from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError


class teamsView(APIView):
    
    
    def post(self, request: Request) -> Response:
        data = request.data
        try:
            data_processing(data)
            new_team = Team.objects.create(**data)
        except IntegrityError:
            return Response({"error": "fifa_code alredy exits"}, status.HTTP_400_BAD_REQUEST) 
        except NegativeTitlesError:
            return Response({"error": "titles cannot be negative"}, status.HTTP_400_BAD_REQUEST)
        except InvalidYearCupError:
            return Response({"error": "there was no world cup this year"}, status.HTTP_400_BAD_REQUEST)
        except ImpossibleTitlesError:
           return Response({"error": "impossible to have more titles than disputed cups"}, status.HTTP_400_BAD_REQUEST)
    
        converted_team = model_to_dict(new_team)
        return Response(converted_team, status.HTTP_201_CREATED)
    
    
    def get(self, request: Request) -> Response:
        teams = Team.objects.all()
        converted_teams = [model_to_dict(team) for team in teams]
        return Response(converted_teams)


class teamsIdView(APIView):
    
    
    
    def get(sef, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except:
            return Response({"error": "Team not found"}, status.HTTP_404_NOT_FOUND)
        converted_team = model_to_dict(team)
        return Response(converted_team)
