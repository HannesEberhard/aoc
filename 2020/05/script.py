
from common import Day


class Day_2020_05(Day):

    def parse(self):
        return super().parse()

    @staticmethod
    def partition(code):
        lower_bound = 0
        upper_bound = int(2 ** len(code)) - 1
        for i in range(len(code)):
            if code[i] in ["F", "L"]:
                upper_bound -= int(2 ** (len(code) - i - 1))
            else:
                lower_bound += int(2 ** (len(code) - i - 1))
        return lower_bound

    def part_1(self):
        max_seat_id = 0
        for code in self.parsed:
            row = self.partition(code[:7])
            column = self.partition(code[-3:])
            seat_id = row * 8 + column
            if seat_id > max_seat_id:
                max_seat_id = seat_id
        return max_seat_id

    def part_2(self):
        taken = set()
        for code in self.parsed:
            row = self.partition(code[:7])
            column = self.partition(code[-3:])
            seat_id = row * 8 + column
            taken.add(seat_id)
        taken = list(taken)
        for i in range(len(taken)):
            if taken[i] != i + taken[0]:
                return i + taken[0]


if __name__ == "__main__":
    Day_2020_05().solve()
