from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
import datetime

def data_processing(data: dict):
    try:
        if data['titles'] < 0:
            raise NegativeTitlesError("Número de títulos não pode ser negativo")
        
        current_year = datetime.datetime.now().year
        valid_years = range(1930, current_year, 4)
        
        if data['first_cup'] not in valid_years:
            raise InvalidYearCupError("Ano de primeira participação inválido para Copa do Mundo")
        
        copes = range(data["first_cup"], current_year, 4)
        number_of_copes = len(copes)
        
        if data["titles"] > number_of_copes:
            raise ImpossibleTitlesError()
        
    except NegativeTitlesError as e:
        raise e
    except InvalidYearCupError as e:
        raise e
    except ImpossibleTitlesError as e:
        raise e
