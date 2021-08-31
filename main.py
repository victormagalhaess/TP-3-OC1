from instruction import Instruction
from cache import Cache
from memory import Memory

'''
64 blocos

0000000000000000000011

6
1000000000000000000011

10101001011000000011

index   validity   tag               data
000000   false
000001   false
000010   false
000011   true     0101001011000     AAAA
...
111111   false
...


index                       data
0000101010010101001         AAAA



– Sua memória de dados consegue armazenar 1024 palavras de 32 bits.
– Sua cache tem a capacidade de armazenar 64 blocos. Cada bloco da cache contém 16 bytes, que
correspondem a 4 palavras de 32 bits, que resultam em 128 bits no total.
– Sua cache utiliza Mapeamento Direto para alocar os blocos.
– Para operações de escrita na memória você deve utilizar a técnica de Write Back.
– Os endereços que a CPU fornece contém 32 bits.
'''

def readFile():
    file = open("in.txt", "r")
    
    return file

def getInstructions(file):
    instructions = []
    for line in file:
        rawData = []
        for word in line.split():
            rawData.append(word)
        adr, op = rawData[:2]
        data = None
        if op == '1':
            data = rawData[2]
        instructions.append(Instruction(adr, op, data))
    return instructions

def closeFile(file):
    file.close()

def main():
    file = readFile()
    instructions = getInstructions(file)
    closeFile(file)
    cache = Cache()
    for block in cache.blocks:
        print(block)

    memory = Memory()
    for word in memory.words:
        print(word)

if __name__ == '__main__':
    main()