import random

class appNoGenerator:
    def __init__(self):
        pass
    @staticmethod
    def appNoGenerator():
        length_start = 1000000000000
        length_end = 9000000000000
        result = str(random.randrange(length_start, length_end))
        return result
