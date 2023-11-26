from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
from datetime import datetime

def data_processing(data: dict):
    if data['titles'] < 0:
        raise NegativeTitlesError("titles cannot be negative")
    
    first_cup_date = datetime.strptime(data['first_cup'], '%Y-%m-%d')
    first_cup_year = first_cup_date.year

    current_year = datetime.now().year
    valid_years = range(1930, current_year, 4)
    
    if first_cup_year not in valid_years:
        raise InvalidYearCupError("there was no world cup this year")
    
    copes = range(first_cup_year, current_year, 4)
    number_of_copes = len(copes)
    
    if data["titles"] > number_of_copes:
        raise ImpossibleTitlesError()
