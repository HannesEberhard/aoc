
from common import Day


class Day_2020_09(Day):

    lenght = 25

    def parse(self):
        return [int(x) for x in super().parse()]

    def is_sum(self, value, inputs):
        for i in range(len(inputs)):
            for j in range(len(inputs)):
                if i != j and inputs[i] + inputs[j] == value:
                    return True
        return False

    def part_1(self):
        for i in range(self.lenght, len(self.parsed)):
            if not self.is_sum(self.parsed[i], self.parsed[i - self.lenght:i]):
                return self.parsed[i]

    def part_2(self):
        for i in range(len(self.parsed)):
            for j in range(i + 2, len(self.parsed)):
                combination_sum = sum(self.parsed[i:j])
                if combination_sum == self.part_1_solution:
                    return min(self.parsed[i:j]) + max(self.parsed[i:j])
                elif combination_sum > self.part_1_solution:
                    break


if __name__ == "__main__":
    Day_2020_09().solve()
