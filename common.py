
import os


class Day:

    def parse(self):
        return self.input.split("\n")

    def read(self):
        with open(f"Day_{self.year}_{self.day}.txt", "r") as f:
            return f.read()

    def part_1(self):
        return "not implemented"

    def part_2(self):
        return "not implemented"

    def solve(self):
        print(f"{self.year}-{self.day} solutions")
        print("=================")
        print()
        print("part 1:")
        self.part_1_solution = self.part_1()
        print(self.part_1_solution)
        print()
        print("part 2:")
        self.part_2_solution = self.part_2()
        print(self.part_2_solution)
        print()

    def __init__(self):
        self.year = type(self).__name__.split("_")[1]
        self.day = type(self).__name__.split("_")[2]
        self.input = self.read()
        self.parsed = self.parse()


class StructureManager:

    @staticmethod
    def __create_year(year):
        if os.path.exists(str(year)):
            raise Exception("Year already exists")
        os.mkdir(str(year))

    @staticmethod
    def __create_script(year, day):
        with open(f"{year}/Day_{year}_{day}.py", "w+") as f:
            f.write(f"""
from common import Day


class Day_{year}_{day}(Day):

    def parse(self):
        return super().parse()

    def part_1(self):
        return None

    def part_2(self):
        return None


if __name__ == "__main__":
    Day_{year}_{day}().solve()
""")

    @staticmethod
    def __create_input(year, day):
        open(f"{year}/Day_{year}_{day}.txt", "w+").close()

    def create(self, year):
        self.__create_year(year)
        for i in range(1, 30):
            day = str(i).zfill(2)
            self.__create_script(year, day)
            self.__create_input(year, day)

