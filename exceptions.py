

class NegativeTitlesError(Exception):
    
    
    def __init__(self, message="titles cannot be negative"):
        self.message = message
        super().__init__(self.message)


class InvalidYearCupError(Exception):
    

    def __init__(self, message="there was no world cup this year"):
        self.message = message
        super().__init__(self.message)


