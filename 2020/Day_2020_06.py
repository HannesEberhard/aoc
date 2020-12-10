
from common import Day
import string


class Day_2020_06(Day):

    def parse(self):
        parsed = []
        for group in self.input.split("\n\n"):
            parsed.append([])
            for person in group.split(("\n")):
                parsed[-1].append(person)
        return parsed

    def part_1(self):
        count = 0
        for group in self.parsed:
            answers = set()
            [answers.update(list(person)) for person in group]
            count += len(answers)
        return count

    def part_2(self):
        count = 0
        for group in self.parsed:
            answers = set(list(string.ascii_lowercase))
            for person in group:
                answers = answers.intersection(list(person))
            count += len(answers)
        return count


if __name__ == "__main__":
    Day_2020_06().solve()
