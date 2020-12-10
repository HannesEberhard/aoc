
from common import Day
import re


class Day_2020_04(Day):

    def parse(self):
        parsed = []
        for passport in self.input.split("\n\n"):
            parsed.append(dict())
            passport = passport.replace("\n", " ")
            for pair in passport.split(" "):
                splitted = pair.split(":")
                parsed[-1][splitted[0]] = splitted[1]
        return parsed

    def part_1(self):
        valid = 0
        for passport in self.parsed:
            if len(passport) == 8 or (len(passport) == 7 and "cid" not in passport):
                valid += 1
        return valid

    def part_2(self):
        valid = 0
        for passport in self.parsed:
            if not (len(passport) == 8 or (len(passport) == 7 and "cid" not in passport)):
                continue
            if not (1920 <= int(passport["byr"]) <= 2002):
                continue
            if not (2010 <= int(passport["iyr"]) <= 2020):
                continue
            if not (2020 <= int(passport["eyr"]) <= 2030):
                continue
            if "cm" not in passport["hgt"] and "in" not in passport["hgt"]:
                continue
            if "cm" in passport["hgt"] and not (150 <= int(passport["hgt"][:-2]) <= 193):
                continue
            if "in" in passport["hgt"] and not (59 <= int(passport["hgt"][:-2]) <= 76):
                continue
            if not re.match("^#([0-9a-f]{6})$", passport["hcl"]):
                continue
            if not passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                continue
            if not re.match("^([0-9]{9})$", passport["pid"]):
                continue
            valid += 1
        return valid


if __name__ == "__main__":
    Day_2020_04().solve()
