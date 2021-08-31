class Memory:
    def __init__(self):
        # 1024 @ 32 bits
        self.words = []
        for index in range(1024):
            word = {
                'index': '{0:010b}'.format(index),
                'data': ''
            }
            self.words.append(word)