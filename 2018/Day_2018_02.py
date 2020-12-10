
from common import Day
from collections import defaultdict


class Day_2018_02(Day):

    def parse(self):
        return super().parse()

    def part_1(self):
        two_count = 0
        three_count = 0
        for id in self.parsed:
            dict = defaultdict(int)
            for letter in id:
                dict[letter] += 1
            if 2 in dict.values():
                two_count += 1
            if 3 in dict.values():
                three_count += 1
        return two_count * three_count

    def part_2(self):
        for i in range(len(self.parsed)):
            for j in range(i + 1, len(self.parsed)):
                diff = ""
                for k in range(len(self.parsed[i])):
                    if self.parsed[i][k] == self.parsed[j][k]:
                        diff += self.parsed[i][k]
                if len(self.parsed[i]) == len(diff) + 1:
                    return diff


if __name__ == "__main__":
    Day_2018_02().solve()
