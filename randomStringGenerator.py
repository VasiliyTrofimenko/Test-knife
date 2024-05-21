import random

class randomStringGen:
    @staticmethod
    def generate_random_string():
        start_length = 1000000000000000000
        end_length = 8999999999999999999
        return str(random.randrange(start_length, end_length))