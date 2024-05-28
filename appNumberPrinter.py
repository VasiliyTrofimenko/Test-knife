
import pyperclip
import appNumberGenerator


class appNumberPrinter:
    @staticmethod
    def appNoPrinter(secondArg):
        gen = appNumberGenerator.appNoGenerator()
        result = '\n'.join([ str(gen) for _ in range(secondArg)])
        pyperclip.copy(result)
        return result.replace('\n', ', ')