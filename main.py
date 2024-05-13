import configparser
import random
import sys
import pyperclip
import json
import xml.etree.ElementTree as ET
from time import strftime
import uuid
from pathlib import Path
import io
import codecs

# Пути к файлам JSON
path = 'C:/Users/vtrofimenko/Desktop/Test-knife/logs.txt'
jsonFPAPath = 'C:\\Users\\vtrofimenko\\Desktop\\tnife\\Tnife-main\\fpaProsses\\FPA.json'
jsonASRPATH = 'C:\\Users\\vtrofimenko\\Desktop\\tnife\\Tnife-main\\arfProsses\\ARF.json'

message = ''' 
-case -count - для генерации caseId для создания дел, при использовании нужно указывать количество генераций 
-json - для еденичной генерации уникальных OrderId,clientId,messageId
-app -count - генерация OrderId, при использовании нужно указывать количество генераций 
-epgu - для генерации json файла с уникальными значениями OrderId,clientId,messageId
    -arf - для генерации заявления АСР
    -fpa - для генерации заявления ЗП
-uuid -count - генерация uuid значений, при использовании нужно указывать количество генераций
'''
Args = sys.argv


def appNoGenerator():
    length_start = 1000000000000
    length_end = 9000000000000
    return str(random.randrange(length_start, length_end))


def printForJson():
    stringUUid = []
    for _ in range(2):
        myUuid = uuid.uuid4()
        stringUUid.append(str(myUuid))
    result = appNoGenerator() + ", " + ', '.join(stringUUid)
    return result


def uuidsCountPrinter(secondArg):
    stringUUid = []
    for _ in range(secondArg):
        myUuid = uuid.uuid4()
        stringUUid.append(str(myUuid))
        result = '\n'.join(stringUUid)
    resultOut = ','.join(stringUUid)
    result = '\n'.join(stringUUid)
    print(str(result))
    return resultOut


def appNoPrinter(secondArg):
    result = '\n'.join([appNoGenerator() for _ in range(secondArg)])
    pyperclip.copy(result)
    return result.replace('\n', ', ')


def copyCoreId(secondArg):
    result = '\n'.join([generate_random_string() for _ in range(secondArg)])
    resultForOut = ', '.join([generate_random_string() for _ in range(secondArg)])
    pyperclip.copy(result)
    return resultForOut


def generate_random_string():
    start_length = 1000000000000000000
    end_length = 8999999999999999999
    return str(random.randrange(start_length, end_length))


def write_log(text):
    current_time = strftime("%Y-%m-%d %H:%M:%S")
    with open(path, 'a') as f:
        f.write(current_time + " >>>> " + str(text) + '\n')


def serGenerator():
    start = 1000
    end = 9999
    return (str(random.randrange(start, end)))


def numberGenerator():
    start = 1000000
    end = 9999999
    return (str(random.randrange(start, end)))

def epgu(secondArg):
    stringUUid = [str(uuid.uuid4()) for _ in range(2)]
    messageId = stringUUid[0]
    clientId = stringUUid[1]
    global orderId_text
    global series_text
    global number_text

    if secondArg == 'arf':
        try:
            with open(jsonASRPATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            return f"File '{jsonASRPATH}' not found."
        except json.JSONDecodeError:
            return f"Error decoding JSON in file '{jsonASRPATH}'."

        data['smevMetadata']['messageId'] = messageId
        data['message']['requestMetadata']['clientId'] = clientId
        xml_data = data['message']['requestContent']['content']['messagePrimaryContent']
        root = ET.fromstring(xml_data)

        for orderId in root.iter('{urn://mvd/gismu/arf/1.1.0}orderId'):
            orderId.text = appNoGenerator()
            orderId_text = orderId.text
            break
        if orderId_text is None:
            orderId_text = ""

        xml_string = ET.tostring(root, encoding='unicode')

        data['message']['requestContent']['content']['messagePrimaryContent'] = xml_string

        with codecs.open(jsonASRPATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return f"messageId = {messageId}, clientId = {clientId}, OrderId = {orderId_text}"

    elif secondArg == 'fpa':
        orderId_text = None
        try:
            with codecs.open(jsonFPAPath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            return f"File '{jsonFPAPath}' not found."
        except json.JSONDecodeError:
            return f"Error decoding JSON in file '{jsonFPAPath}'."

        data['smevMetadata']['messageId'] = messageId
        data['message']['requestMetadata']['clientId'] = clientId
        xmlData = data['message']['requestContent']['content']['messagePrimaryContent']
        root = ET.fromstring(xmlData)

        namespace0 = {'ns0': 'urn://mvd/gismu/FPA/EPGU/1.0.6'}
        namespace1 = {'ns1': 'urn://mvd/gismu/FPA/EPGU/types/1.0.6'}

        for orderId in root.findall('.//ns0:OrderId', namespace0):
            orderId.text = appNoGenerator()
            orderId_text = orderId.text
            break

        if orderId_text is None:
            orderId_text = ""

        for series in root.findall('.//ns1:Series', namespace1):
            series.text = serGenerator()
            series_text = series.text
            break

        for number in root.findall('.//ns1:Number', namespace1):
            number.text = numberGenerator()
            number_text = number.text
            break

        xml_string = ET.tostring(root, encoding='unicode')

        data['message']['requestContent']['content']['messagePrimaryContent'] = xml_string

        with codecs.open(jsonFPAPath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        return f"messageId = {messageId}, clientId = {clientId}, OrderId = {orderId_text} , Series = {series_text} , Number = {number_text}"


if len(Args) > 1:
    if Args[1] == "-json":
        write_log(printForJson())
    elif Args[1] == "-case":
        if len(Args) > 2:
            write_log(copyCoreId(int(Args[2])))
        else:
            print("Недостаточно аргументов для -case.")
    elif Args[1] == "-app":
        if len(Args) > 2:
            write_log(appNoPrinter(int(Args[2])))
        else:
            print("Недостаточно аргументов для -app.")
    elif Args[1] == "-epgu":
        if len(Args) > 2:
            write_log(epgu(str(Args[2])))
        else:
            print("Недостаточно аргументов для -epgu.")
    elif Args[1] == "-uuid":
        if len(Args) > 2:
            write_log(uuidsCountPrinter(int(Args[2])))
        else:
            print("Недостаточно аргументов для -uuid.")
    else:
        print(message)
else:
    print(message)
