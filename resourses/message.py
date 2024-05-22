
class Message:
    def __init__(self,message) -> None:
        self.message = message
    @staticmethod
    def defautMessage():
        message = ''' 
                -case -count - для генерации caseId для создания дел, при использовании нужно указывать количество генераций 
                -json - для еденичной генерации уникальных OrderId,clientId,messageId
                -app -count - генерация OrderId, при использовании нужно указывать количество генераций 
                -epgu - для генерации json файла с уникальными значениями OrderId,clientId,messageId
                    -arf - для генерации заявления АСР
                    -fpa - для генерации заявления ЗП
                -uuid -count - генерация uuid значений, при использовании нужно указывать количество генераций
                '''
        return message