
from common import Day
from itertools import permutations

class Day_2020_01(Day):

    def parse(self):
        return [int(x) for x in super().parse()]

    def part_1(self):
        for tuple in permutations(self.parsed, 2):
            if sum(tuple) == 2020:
                return tuple[0] * tuple[1]

    def part_2(self):
        for triple in permutations(self.parsed, 3):
            if sum(triple) == 2020:
                return triple[0] * triple[1] * triple[2]


if __name__ == "__main__":
    Day_2020_01().solve()
