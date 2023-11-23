

class NegativeTitlesError(Exception):
    
    
    def __init__(self, message="titles cannot be negative"):
        self.message = message
        super().__init__(self.message)


