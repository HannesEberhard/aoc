
from common import Day


class Day_2020_02(Day):

    def parse(self):
        parsed = []
        for line in super().parse():
            splitted = line.split(" ")
            range = [int(x) for x in splitted[0].split("-")]
            character = splitted[1][:-1]
            password = splitted[2]
            parsed.append([range, character, password])
        return parsed

    def part_1(self):
        correct = 0
        for line in self.parsed:
            character_count = line[2].count(line[1])
            if line[0][0] <= character_count <= line[0][1]:
                correct += 1
        return correct

    def part_2(self):
        correct = 0
        for line in self.parsed:
            if bool(line[2][line[0][0] - 1] == line[1]) is not bool(line[2][line[0][1] - 1] == line[1]):
                correct += 1
        return correct


if __name__ == "__main__":
    Day_2020_02().solve()
