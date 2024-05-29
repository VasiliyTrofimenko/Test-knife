from kafka import KafkaProducer
from kafka.errors import KafkaError
import configparser
import json
import codecs
import logging
logging.basicConfig(level=logging.INFO)



class kafkaSenderClass:
    @staticmethod
    def kafkaSender(second_arg):
        config = configparser.ConfigParser()
        config.read('config.ini')
        kafkaServer = config.get('Kafka','bootstrap_servers')
        producer = KafkaProducer(bootstrap_servers=kafkaServer,value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        match second_arg:
            case 'fpa':
                configPath = config.get('Path', 'FPA')
                try:
                    with codecs.open(configPath, 'r', encoding='utf-8') as f:
                        message = json.load(f)
                        producer.send('fpaEpguRequest', message)
                        producer.flush()
                except FileNotFoundError:
                    return f"File '{configPath}' not found."
                except json.JSONDecodeError:
                        return f"Error decoding JSON in file '{configPath}'."
                return f"Succses! Message delivered!"
            case 'arf':
                configPath = config.get('Path', 'ASR')
                try:
                    with codecs.open(configPath, 'r', encoding='utf-8') as f:
                        message = json.load(f)
                        producer.send('arfEPGURequestQueue', message)
                        producer.flush()
                except FileNotFoundError:
                        return f"File '{configPath}' not found."
                except json.JSONDecodeError:
                        return f"Error decoding JSON in file '{configPath}'."
                return f"Succses! Message delivered!"
                
