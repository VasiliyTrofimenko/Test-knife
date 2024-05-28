import random

class serialNoGenerator:
    @staticmethod
    def serGenerator():
        start = 1000
        end = 9999
        return (str(random.randrange(start, end)))
