class Instruction:
    def __init__(self, adr, op, data):
        self.adr = int(adr)
        self.op = op
        self.data = data
        self.result = ""

    def getAdr(self):
        return self.adr

    def isOpWrite(self):
        return self.op == '1'

    def getData(self):
        if not self.data:
            print('No data related to instruction.')
            return 0
        else:
            return self.data
