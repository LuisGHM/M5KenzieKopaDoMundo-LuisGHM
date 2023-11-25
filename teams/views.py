from rest_framework.views import APIView, Request, Response, status
from teams.models import Team
from django.db import IntegrityError
from django.forms import model_to_dict
from utils import data_processing
from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError


class teamsView(APIView):
    
    
    def post(self, request: Request):
        data = request.data
        try:
            data_processing(data)
            new_team = Team.objects.create(**data)
        except IntegrityError:
            return Response({"error": "fifa_code alredy exits"}, status.HTTP_400_BAD_REQUEST) 
        except NegativeTitlesError:
            return Response({"error": "titles cannot be negative"}, status.HTTP_400_BAD_REQUEST)
        except InvalidYearCupError as e:
            return Response({"error": "there was no world cup this year"}, status.HTTP_400_BAD_REQUEST)
        except ImpossibleTitlesError as e:
           return Response({"error": "impossible to have more titles than disputed cups"}, status.HTTP_400_BAD_REQUEST)
    
        converted_team = model_to_dict(new_team)
        return Response(converted_team, status.HTTP_201_CREATED)