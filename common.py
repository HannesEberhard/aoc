
import os


class Day:

    def parse(self):
        return self.input.split("\n")

    def read(self):
        with open(f"input.txt", "r") as f:
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
        with open(f"{year}/{day}/script.py", "w+") as f:
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
        open(f"{year}/{day}/input.txt", "w+").close()

    def create(self, year):
        self.__create_year(year)
        for i in range(1, 26):
            day = str(i).zfill(2)
            os.mkdir(f"{year}/{day}")
            self.__create_script(year, day)
            self.__create_input(year, day)


    def migrate(self, year):
        self.__create_year(f"{year}_migrated")
        for i in range(1, 26):
            day = str(i).zfill(2)
            os.mkdir(f"{year}_migrated/{day}")
            os.rename(f"{year}/Day_{year}_{day}.py", f"{year}_migrated/{day}/script.py")
            os.rename(f"{year}/Day_{year}_{day}.txt", f"{year}_migrated/{day}/input.txt")


