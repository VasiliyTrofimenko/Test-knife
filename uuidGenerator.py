import uuid

class uuidGenerator:
    @staticmethod
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