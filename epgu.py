import codecs
import json
import uuid
from appNumberGenerator import appNoGenerator
from randomStringGenerator import randomStringGen
from serialNumberGenerator import serialNoGenerator
from numberGenerator import numberGenerator
import xml.etree.ElementTree as ET

# сделать передачу аргумета пути, возможно засунуть в switch
class EPGU:
    @staticmethod
    def epgu(secondArg):
        jsonFPAPath = 'C:\\Users\\vtrofimenko\\Desktop\\tnife\\Tnife-main\\fpaProsses\\FPA.json'
        jsonASRPATH = 'C:\\Users\\vtrofimenko\\Desktop\\Test-knife\\arfProsses\\ARF.json'
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
                orderId.text = appNoGenerator.appNoGenerator()
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
                orderId.text = appNoGenerator.appNoGenerator()
                orderId_text = orderId.text
                break

            if orderId_text is None:
                orderId_text = ""

            for series in root.findall('.//ns1:Series', namespace1):
                series.text = serialNoGenerator.serGenerator()
                series_text = series.text
                break

            for number in root.findall('.//ns1:Number', namespace1):
                number.text = numberGenerator.numberGenerator()
                number_text = number.text
                break

            xml_string = ET.tostring(root, encoding='unicode')

            data['message']['requestContent']['content']['messagePrimaryContent'] = xml_string

            with codecs.open(jsonFPAPath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

            return f"messageId = {messageId}, clientId = {clientId}, OrderId = {orderId_text} , Series = {series_text} , Number = {number_text}"
    