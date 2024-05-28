import uuid
import appNumberGenerator

class printForJson:
    @staticmethod
    def printForJson():
        stringUUid = []
        for _ in range(2):
            myUuid = uuid.uuid4()
            stringUUid.append(str(myUuid))
        result = appNumberGenerator.appNoGenerator.appNoGenerator() + ", " + ', '.join(stringUUid)
        return result