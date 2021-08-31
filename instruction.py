class Instruction:
    def __init__(self, adr, op, data):
        self.adr = adr
        self.op = op
        self.data = data

    def getAdr(self):
        return self.adr
    
    def getOp(self):
        return self.op
    
    def getData(self):
        if not self.data:
            print('No data related to instruction.')
            return 0
        else:    
            return self.data