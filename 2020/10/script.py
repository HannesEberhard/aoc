
from common import Day
from collections import defaultdict
from math import ceil


class Day_2020_10(Day):

    def parse(self):
        return sorted([int(x) for x in super().parse()])

    def visualize(self):
        empty = "░"
        filled = "█"
        for adapter in self.parsed:
            line = ([empty] * (max(adapter - 3, 0)) + [filled] * min(adapter, 3) + [empty] * (self.parsed[-1] - adapter))
            print("".join(str(x) for x in line))

    def part_1(self):
        self.visualize()
        differences = [0] * 3 + [1]
        joltage = 0
        for adapter in self.parsed:
            differences[adapter - joltage] += 1
            joltage = adapter
        return differences[1] * differences[3]

    def part_2(self):
        block_sizes = defaultdict(int)
        joltage = 0
        counter = 1
        for adapter in self.parsed:
            difference = adapter - joltage
            joltage = adapter
            if difference == 1:
                counter += 1
            elif difference == 3:
                block_sizes[counter] += 1
                counter = 1
            else:
                raise Exception()
        block_sizes[counter] += 1
        combinations = 1
        for block_size in block_sizes:
            block_size_combinations = max(2 ** (block_size - 2), 1) - max(ceil((block_size + 2 - 6) / 3), 0)
            combinations *= block_size_combinations ** block_sizes[block_size]
        return combinations


if __name__ == "__main__":
    Day_2020_10().solve()
