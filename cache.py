import math


class Cache:
    def __init__(self, memory):
        # 64 @ 16 byts
        self.byteOffset = 2
        self.wordOffset = 2
        self.indexSize = 6
        self.blockSize = 16
        self.numberOfBlocks = 64
        self.blocks = []
        self.memory = memory
        for index in range(self.numberOfBlocks):
            block = {
                'index': '{0:06b}'.format(index),
                'valid': False,
                'dirty': False,
                'tag': '',
                'data': ['', '', '', '']
            }
            self.blocks.append(block)

    def findMapping(self, address):
        blockAdr = math.floor(address/self.blockSize)
        blockNumber = blockAdr % self.numberOfBlocks
        return blockNumber

    def read(self, address):
        blockIndex = (address >> (self.byteOffset +
                      self.wordOffset)) % (1 << self.indexSize)
        tag = address >> (self.byteOffset + self.wordOffset + self.indexSize)
        # todo
        readingBlock = self.blocks[blockIndex]
        if readingBlock['valid'] and readingBlock['tag'] == tag:
            return True  # hit
        else:
            if readingBlock['dirty']:
                for wordIndex, word in enumerate(readingBlock['data']):
                    dirtyAddress = readingBlock['tag']
                    dirtyAddress = dirtyAddress << (
                        self.byteOffset + self.wordOffset + self.indexSize)
                    dirtyAddress += blockIndex << (
                        self.byteOffset + self.wordOffset)
                    dirtyAddress += wordIndex << self.wordOffset
                    dirtyAddress += address % (1 << self.byteOffset)
                    self.memory.write(
                        dirtyAddress, readingBlock['data'][wordIndex])

            readingBlock['valid'] = True
            readingBlock['dirty'] = False
            readingBlock['tag'] = tag

            for wordIndex, word in enumerate(readingBlock['data']):
                newAddress = address >> (self.byteOffset + self.wordOffset)
                newAddress = newAddress << self.wordOffset
                newAddress += wordIndex
                newAddress = newAddress << self.byteOffset
                newAddress += address % (1 << self.byteOffset)
                readingBlock['data'][wordIndex] = self.memory.read(newAddress)

            return False  # miss

    def write(self, address, data):
        newWordIndex = (address >> self.byteOffset) % (1 << self.wordOffset)
        blockIndex = (address >> (self.byteOffset +
                      self.wordOffset)) % (1 << self.indexSize)
        tag = address >> (self.byteOffset + self.wordOffset + self.indexSize)
        # todo
        writingBlock = self.blocks[blockIndex]
        if writingBlock['valid'] and writingBlock['tag'] == tag:
            writingBlock['data'][newWordIndex] = data
            writingBlock['dirty'] = True
        else:
            if writingBlock['dirty']:
                for wordIndex, word in enumerate(writingBlock['data']):
                    dirtyAddress = writingBlock['tag']
                    dirtyAddress = dirtyAddress << (
                        self.byteOffset + self.wordOffset + self.indexSize)
                    dirtyAddress += blockIndex << (
                        self.byteOffset + self.wordOffset)
                    dirtyAddress += wordIndex << self.wordOffset
                    dirtyAddress += address % (1 << self.byteOffset)
                    self.memory.write(
                        dirtyAddress, writingBlock['data'][wordIndex])

            writingBlock['valid'] = True
            writingBlock['dirty'] = False
            writingBlock['tag'] = tag
            for wordIndex, word in enumerate(writingBlock['data']):
                if wordIndex == newWordIndex:
                    writingBlock['data'][wordIndex] = data
                    continue

                newAddress = address >> (self.byteOffset + self.wordOffset)
                newAddress = newAddress << self.wordOffset
                newAddress += wordIndex
                newAddress = newAddress << self.byteOffset
                newAddress += address % (1 << self.byteOffset)
                writingBlock['data'][wordIndex] = self.memory.read(newAddress)
