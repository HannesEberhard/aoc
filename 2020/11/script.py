
from common import Day
from copy import deepcopy


class Day_2020_11(Day):

    def parse(self):
        temp = [["."] + list(row) + ["."] for row in super().parse()]
        return [["."] * len(temp[0])] + temp + [["."] * len(temp[0])]

    def part_1_count_occupied_seats(self, x, y):
        occupied_seats = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if not (dx == 0 and dy == 0):
                    if self.current_state[y + dy][x + dx] == "#":
                        occupied_seats += 1
        return occupied_seats

    def part_2_count_occupied_seats(self, x, y):
        occupied_seats = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if not (dx == 0 and dy == 0):
                    scale = 1
                    while True:
                        _x = x + scale * dx
                        _y = y + scale * dy
                        if not (_x in range(1, len(self.current_state[0]) - 1) and _y in range(1, len(self.current_state) - 1)):
                            break
                        elif self.current_state[_y][_x] == "#":
                            occupied_seats += 1
                            break
                        elif self.current_state[_y][_x] == "L":
                            break
                        else:
                            scale += 1
        return occupied_seats

    def simulate(self, part):
        changed = False
        result = deepcopy(self.current_state)
        for y in range(1, len(self.current_state) - 1):
            for x in range(1, len(self.current_state[0]) - 1):
                if self.parsed[y][x] == ".":
                    continue
                if part == 1:
                    occupied_seats = self.part_1_count_occupied_seats(x, y)
                else:
                    occupied_seats = self.part_2_count_occupied_seats(x, y)
                if self.current_state[y][x] == "L" and occupied_seats == 0:
                    result[y][x] = "#"
                    changed = True
                elif self.current_state[y][x] == "#" and occupied_seats >= 4 + (part - 1):
                    result[y][x] = "L"
                    changed = True
        self.current_state = result
        return changed

    def part_1(self):
        self.current_state = deepcopy(self.parsed)
        while self.simulate(1):
            pass
        return sum(row.count("#") for row in self.current_state)

    def part_2(self):
        self.current_state = deepcopy(self.parsed)
        while self.simulate(2):
            pass
        return sum(row.count("#") for row in self.current_state)


if __name__ == "__main__":
    Day_2020_11().solve()
