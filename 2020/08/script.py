
from common import Day


class Day_2020_08(Day):

    def parse(self):
        self.interpreter = InstructionInterpreter(self.input)

    def flip_jmp_nop(self, index):
        if self.interpreter.instructions[index][0] == "jmp":
            self.interpreter.instructions[index][0] = "nop"
        elif self.interpreter.instructions[index][0] == "nop":
            self.interpreter.instructions[index][0] = "jmp"

    def part_1(self):
        self.interpreter.terminates()
        return self.interpreter.accumulator

    def part_2(self):
        jmp_nop_instructions = []
        for i in range(len(self.interpreter.instructions)):
            if self.interpreter.instructions[i][0] in ["jmp", "nop"]:
                jmp_nop_instructions.append(i)
        for index in jmp_nop_instructions:
            self.flip_jmp_nop(index)
            if self.interpreter.terminates():
                return self.interpreter.accumulator
            self.flip_jmp_nop(index)


class InstructionInterpreter:

    accumulator = 0
    pointer = 0

    @staticmethod
    def parse(instructions):
        if type(instructions) == str:
            instructions = instructions.split("\n")
        if type(instructions[0]) == list:
            return instructions
        return [instruction.split(" ") for instruction in instructions]

    def step(self):
        operation = self.instructions[self.pointer][0]
        argument = int(self.instructions[self.pointer][1])
        if operation == "acc":
            self.accumulator += argument
            self.pointer += 1
        elif operation == "jmp":
            self.pointer += argument
        elif operation == "nop":
            self.pointer += 1
        return self.pointer < len(self.instructions)

    def execute(self, pointer=0, accumulator=0):
        self.pointer = pointer
        self.accumulator = accumulator
        while self.step():
            pass

    def terminates(self):
        self.pointer = 0
        self.accumulator = 0
        executed = [False] * len(self.instructions)
        while True:
            if executed[self.pointer]:
                return False
            executed[self.pointer] = True
            if self.step() == False:
                return self.pointer == len(self.instructions)

    def __init__(self, instructions):
        self.instructions = self.parse(instructions)


if __name__ == "__main__":
    Day_2020_08().solve()
