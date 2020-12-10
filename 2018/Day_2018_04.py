
from common import Day


class Day_2018_04(Day):

    def parse(self):
        for line in sorted(super().parse()):
            print(line)
        return super().parse()

    def part_1(self):
        return None

    def part_2(self):
        return None


if __name__ == "__main__":
    Day_2018_04().solve()
