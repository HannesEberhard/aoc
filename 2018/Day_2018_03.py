
from common import Day


class Day_2018_03(Day):

    @staticmethod
    def init_fabric(size):
        fabric = []
        for i in range(size):
            fabric.append([0] * size)
        return fabric

    def parse(self):
        parsed = []
        for line in super().parse():
            splitted = line.split(" ")
            origin = [int(x) for x in splitted[2][:-1].split(",")]
            size = [int(x) for x in splitted[3].split("x")]
            parsed.append([origin, size])
        return parsed

    def part_1(self):
        self.fabric = self.init_fabric(2000)
        for id in range(len(self.parsed)):
            x = self.parsed[id][0][0]
            y = self.parsed[id][0][1]
            width = self.parsed[id][1][0]
            height = self.parsed[id][1][1]
            for h in range(height):
                for w in range(width):
                    self.fabric[y + h][x + w] += 1
        return sum(sum(element > 1 for element in row) for row in self.fabric)

    def part_2(self):
        for id in range(len(self.parsed)):
            x = self.parsed[id][0][0]
            y = self.parsed[id][0][1]
            width = self.parsed[id][1][0]
            height = self.parsed[id][1][1]
            total = 0
            for h in range(height):
                total += sum(self.fabric[y + h][x:x+width])
            if total - width * height == 0:
                return id + 1 # ids in input are 1-indexed
        return None


if __name__ == "__main__":
    Day_2018_03().solve()
