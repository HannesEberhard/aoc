
from common import Day
from functools import reduce


class Day_2020_13(Day):

    def parse(self):
        lines = super().parse()
        return [int(lines[0]), lines[1].split(",")]

    def chinese_remainder(self, moduli, remainders):
        sum = 0
        product = reduce(lambda a, b: a * b, moduli)
        for moduli_i, remainders_i in zip(moduli, remainders):
            p = product // moduli_i
            sum += remainders_i * self.multiplicative_inverse(p, moduli_i) * p
        return sum % product

    def multiplicative_inverse(self, a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1:
            return 1
        while a > 1:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += b0
        return x1

    def part_1(self):
        min_waiting_time = 2 ** 32
        min_waiting_id = 0
        for bus in self.parsed[1]:
            if bus != "x":
                waiting_time = int(bus) - self.parsed[0] % int(bus)
                if waiting_time < min_waiting_time:
                    min_waiting_time = waiting_time
                    min_waiting_id = int(bus)
        return min_waiting_time * min_waiting_id

    def part_2(self):
        remainders = []
        moduli = []
        for i in range(len(self.parsed[1])):
            if self.parsed[1][i] != "x":
                remainders.append(int(self.parsed[1][i]) - i)
                moduli.append(int(self.parsed[1][i]))
        return self.chinese_remainder(moduli, remainders)


if __name__ == "__main__":
    Day_2020_13().solve()
