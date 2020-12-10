
from common import Day
import math


class Day_2020_03(Day):

    def parse(self):
        parsed = []
        for line in super().parse():
            parsed.append([(1 if x == "#" else 0) for x in line])
        return parsed

    def traverse(self, dx, dy):
        x = dx
        y = dy
        encountered_trees = 0
        while y < len(self.parsed):
            encountered_trees += self.parsed[y][x]
            x += dx
            y += dy
            x %= len(self.parsed[0])
        return encountered_trees

    def part_1(self):
        return self.traverse(3, 1)

    def part_2(self):
        deltas = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        return math.prod(self.traverse(delta[0], delta[1]) for delta in deltas)


if __name__ == "__main__":
    Day_2020_03().solve()
