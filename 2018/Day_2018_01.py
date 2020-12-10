
from common import Day


class Day_2018_01(Day):

    def parse(self):
        return [int(x[1:]) * (-1 if x[0] == "-" else 1) for x in super().parse()]

    def part_1(self):
        return sum(self.parsed)

    def part_2(self):
        current = 0
        history = set([0])
        i = 0
        while True:
            current += self.parsed[i % len(self.parsed)]
            if current in history:
                return current
            history.add(current)
            i += 1


if __name__ == "__main__":
    Day_2018_01().solve()
