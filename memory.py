class Memory:
    def __init__(self):
        # 1024 @ 32 bits
        self.byteOffset = 4  # ainda não sei exatamente pq, mas tal qual slide da aula de memória
        self.numberOfWords = 1024
        self.words = []
        for index in range(self.numberOfWords):
            word = {
                'index': '{0:010b}'.format(index),
                'data': []  # tecnicamente só pode armazenar 32 bits
            }
            self.words.append(word)

    def read(self, address):
        return self.words[address >> self.byteOffset]

    def write(self, address, data):
        self.words[address >> self.byteOffset]['data'] = data
