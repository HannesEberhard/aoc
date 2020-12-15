
from common import Day
from collections import defaultdict


class Day_2020_15(Day):

    def parse(self):
        return [int(x) for x in self.input.split(",")]

    def simulate(self, initialization, n):
        history = dict()
        for turn in range(1, len(initialization) + 1):
            number = initialization[turn - 1]
            history[number] = [turn]
        for turn in range(1 + len(initialization), n + 1):
            if len(history[number]) != 2:
                number = 0
            else:
                number = history[number][1] - history[number][0]
            if number in history:
                history[number].append(turn)
            else:
                history[number] = [turn]
            if len(history[number]) == 3:
                history[number] = history[number][1:3]
        return number


    def part_1(self):
        return self.simulate(self.parsed, 2020)

    def part_2(self):
        return self.simulate(self.parsed, 30000000)


if __name__ == "__main__":
    Day_2020_15().solve()
