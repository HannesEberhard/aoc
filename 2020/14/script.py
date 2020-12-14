
from common import Day


class Day_2020_14(Day):

    def parse(self):
        return [x.split(" = ") for x in super().parse()]

    def set_bit(self, value, index):
        return value | (1 << index)

    def clear_bit(self, value, index):
        return value & ~(1 << index)

    def update_mask_part_1(self, value):
        and_mask = 0
        or_mask = 0
        for v in value:
            and_mask <<= 1
            or_mask <<= 1
            if v != '0':
                and_mask |= 1
            if v == '1':
                or_mask |= 1
        return and_mask, or_mask

    def update_memory_part_1(self, memory, address, value, and_mask, or_mask):
        memory[address] = (value & and_mask) | or_mask
        return memory

    def update_mask_part_2(self, value):
        or_mask = 0
        floating = []
        for i, v in enumerate(value):
            or_mask <<= 1
            if v == '1':
                or_mask |= 1
            elif v == 'X':
                floating.append(len(value) - i - 1)
        return or_mask, floating

    def update_memory_part_2(self, memory, address, value, or_mask, floating):
        address |= or_mask
        for i in range(2 ** len(floating)):
            floating_address = address
            for j in range(len(floating)):
                bit = (i >> j) & 1
                if bit == 0:
                    floating_address = self.clear_bit(floating_address, floating[j])
                else:
                    floating_address = self.set_bit(floating_address, floating[j])
            memory[floating_address] = value
        return memory

    def part_1(self):
        memory = dict()
        for instruction in self.parsed:
            if instruction[0] == "mask":
                and_mask, or_mask = self.update_mask_part_1(instruction[1])
            else:
                memory = self.update_memory_part_1(memory, int(instruction[0][4:-1]), int(instruction[1]), and_mask, or_mask)
        return sum(memory.values())

    def part_2(self):
        memory = dict()
        for instruction in self.parsed:
            if instruction[0] == "mask":
                or_mask, floating = self.update_mask_part_2(instruction[1])
            else:
                memory = self.update_memory_part_2(memory, int(instruction[0][4:-1]), int(instruction[1]), or_mask, floating)
        return sum(memory.values())


if __name__ == "__main__":
    Day_2020_14().solve()
