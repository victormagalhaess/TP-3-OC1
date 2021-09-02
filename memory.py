class Memory:
    def __init__(self):
        # 1024 @ 32 bits
        self.byteOffset = 4
        self.numberOfWords = 1024
        self.words = []
        for index in range(self.numberOfWords):
            word = {
                'index': '{0:010b}'.format(index),
                'data': []
            }
            self.words.append(word)

    def read(self, address):
        return self.words[address >> self.byteOffset]

    def write(self, address, data):
        self.words[address >> self.byteOffset]['data'] = data
