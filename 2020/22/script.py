
from common import Day
from copy import deepcopy


class Day_2020_22(Day):

    history = []

    def parse(self):
        players = []
        for player in self.input.split("\n\n"):
            players.append([int(x) for x in player.split("\n")[1:]])
        return players

    def step(self, a, b, part):
        if part == 2:
            config = (tuple(a), tuple(b))
            if config in self.history[-1]:
                b.clear()
                return a, b
            else:
                self.history[-1].add(config)
        a_top = a.pop(0)
        b_top = b.pop(0)
        if part == 2 and len(a) >= a_top and len(b) >= b_top:
            a_sub = a[:a_top]
            b_sub = b[:b_top]
            a_sub, b_sub = self.play(a_sub, b_sub, 2)
            recursive = True
        else:
            recursive = False
        if not recursive and a_top > b_top or recursive and len(b_sub) == 0:
            a.append(a_top)
            a.append(b_top)
        else:
            b.append(b_top)
            b.append(a_top)
        return a, b

    def play(self, a, b, part):
        if part == 2:
            self.history.append(set())
        while len(a) > 0 and len(b) > 0:
            a, b = self.step(a, b, part)
        if part == 2:
            self.history.pop()
        return a, b

    def calculate_score(self, cards):
        return sum((len(cards) - i) * v for i, v in enumerate(cards))

    def part_1(self):
        a, b = deepcopy(self.parsed)
        a, b = self.play(a, b, 1)
        return self.calculate_score(a if len(a) > 0 else b)

    def part_2(self):
        a, b = deepcopy(self.parsed)
        a, b = self.play(a, b, 2)
        return self.calculate_score(a if len(a) > 0 else b)


if __name__ == "__main__":
    Day_2020_22().solve()
