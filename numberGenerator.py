import random
class numberGenerator:
    @staticmethod
    def numberGenerator():
        start = 1000000
        end = 9999999
        return (str(random.randrange(start, end)))