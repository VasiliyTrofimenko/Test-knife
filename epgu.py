import codecs
import json
import uuid
from appNumberGenerator import appNoGenerator
from serialNumberGenerator import serialNoGenerator
from numberGenerator import numberGenerator
import xml.etree.ElementTree as ET
import configparser


class EPGU:
    @staticmethod
    def epgu(secondArg):
        config = configparser.ConfigParser()
        config.read('config.ini')
        FPAconfig = config.get('Path','FPA')
        ARFconfig = config.get('Path','ASR')
        stringUUid = [str(uuid.uuid4()) for _ in range(2)]
        messageId = stringUUid[0]
        clientId = stringUUid[1]
        global orderId_text
        global series_text
        global number_text

        if secondArg == 'arf':
            try:
                with open(ARFconfig, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except FileNotFoundError:
                return f"File '{ARFconfig}' not found."
            except json.JSONDecodeError:
                return f"Error decoding JSON in file '{ARFconfig}'."

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

            with codecs.open(ARFconfig, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            return f"messageId = {messageId}, clientId = {clientId}, OrderId = {orderId_text}"

        elif secondArg == 'fpa':
            orderId_text = None
            try:
                with codecs.open(FPAconfig, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except FileNotFoundError:
                return f"File '{FPAconfig}' not found."
            except json.JSONDecodeError:
                return f"Error decoding JSON in file '{FPAconfig}'."

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

            with codecs.open(FPAconfig, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

            return f"messageId = {messageId}, clientId = {clientId}, OrderId = {orderId_text} , Series = {series_text} , Number = {number_text}"
    