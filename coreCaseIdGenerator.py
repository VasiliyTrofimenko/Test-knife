import pyperclip
import randomStringGenerator

class coreCaseIdGenerator:
    @staticmethod
    def copyCoreId(secondArg):
        result = '\n'.join([randomStringGenerator.randomStringGen.generate_random_string() for _ in range(secondArg)])
        pyperclip.copy(result)
        return result.replace('\n', ', ')