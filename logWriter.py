from time import strftime

class logWriter:
    @staticmethod
    def write_log(text):
        _path = 'C:/Users/vtrofimenko/Desktop/Test-knife/logs.txt'
        current_time = strftime("%Y-%m-%d %H:%M:%S")
        with open(_path, 'a') as f:
            f.write(current_time + " >>>> " + str(text) + '\n')