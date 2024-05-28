from time import strftime
import configparser
class logWriter:
    @staticmethod
    def write_log(text):
        config = configparser.ConfigParser()
        config.read('config.ini')
        _path = config.get('Path','logs_path')
        current_time = strftime("%Y-%m-%d %H:%M:%S")
        with open(_path, 'a') as f:
            f.write(current_time + " >>>> " + str(text) + '\n')