from instruction import Instruction
from cache import Cache
from memory import Memory
from cpu import Cpu

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
        data = ""
        if op == '1':
            data = rawData[2]
        instructions.append(Instruction(adr, op, data))
    return instructions

def closeFile(file):
    file.close()

def assembleResponse(instructions, cpu):
    with open("result.txt", "w") as result:
        result.write("""READS: {}
WRITES: {}
HITS: {}
MISSES: {}
HIT RATE: {}
MISS RATE: {}\n\n""".format(cpu.reads, cpu.writes, cpu.hits, cpu.misses, cpu.hitRate, cpu.missRate))
        for instruction in instructions:
            result.write("{} {} {} {}\n".format(instruction.adr, instruction.op, instruction.data, instruction.result))

def main():
    file = readFile()
    instructions = getInstructions(file)
    closeFile(file)
    memory = Memory()
    cache = Cache(memory)
    cpu = Cpu(cache, memory)

    for instruction in instructions:
        cpu.process(instruction)

    assembleResponse(instructions, cpu)

    memory.write(20, "teste")
    print(memory.read(20))

    print(cache.findMapping(1200))


if __name__ == '__main__':
    main()