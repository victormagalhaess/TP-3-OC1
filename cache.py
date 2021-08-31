class Cache:
    def __init__(self):
        # 64 @ 16 byts
        self.blocks = []
        for index in range(64):
            block = {
                'index': '{0:06b}'.format(index),
                'validity': False,
                'tag': '',
                'data': ''
            }
            self.blocks.append(block)
        