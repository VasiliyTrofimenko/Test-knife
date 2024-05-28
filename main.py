import sys
from printForJson import printForJson
from coreCaseIdGenerator import coreCaseIdGenerator
from appNumberPrinter import appNumberPrinter
from uuidGenerator import uuidGenerator
from epgu import EPGU
from logWriter import logWriter
from resourses.message import Message
from kafkaSender import kafkaSenderClass

Args = sys.argv

if __name__ == '__main__':
    if len(Args) > 1:
        if Args[1] == "-json":
            logWriter.write_log(printForJson.printForJson())
        elif Args[1] == "-case":
            if len(Args) > 2:
                logWriter.write_log(coreCaseIdGenerator.copyCoreId(int(Args[2])))
            else:
                print("Недостаточно аргументов для -case.")
        elif Args[1] == "-app":
            if len(Args) > 2:
                logWriter.write_log(appNumberPrinter.appNoPrinter(int(Args[2])))
            else:
                print("Недостаточно аргументов для -app.")
        elif Args[1] == "-epgu":
            
            if len(Args) > 3:
                logWriter.write_log(EPGU.epgu(str(Args[2])))
            else:
                print("Недостаточно аргументов для -epgu.")
        elif Args[1] == "-uuid":
            if len(Args) > 2:
                logWriter.write_log(uuidGenerator.uuidsCountPrinter(int(Args[2])))
            else:
                print("Недостаточно аргументов для -uuid.")
        else:
            print(Message.defautMessage())
    else:
        print(Message.defautMessage())
