import math

class Cache:
    def __init__(self, memory):
        # 64 @ 16 byts
        self.byteOffset = 4
        self.indexSize = 6
        self.blockSize = 16
        self.numberOfBlocks = 64
        self.blocks = []
        self.memory = memory
        for index in range(self.numberOfBlocks):
            block = {
                'index': '{0:06b}'.format(index),
                'validity': False,
                'dirty': False,
                'tag': '',
                'data': ""
            }
            self.blocks.append(block)
        
    
    def findMapping(self, address):
        blockAdr = math.floor(address/self.blockSize)
        blockNumber = blockAdr % self.numberOfBlocks
        return blockNumber

    
    def read(self, address):
        blockIndex = (address >> (self.byteOffset)) % 1 << self.indexSize
        tag = address >> (self.byteOffset + self.indexSize)
        #todo




    def write(self, address, data):
        blockIndex = (address >> (self.byteOffset)) % 1 << self.indexSize
        tag = address >> (self.byteOffset + self.indexSize)
        #todo

        