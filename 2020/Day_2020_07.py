
from common import Day


class Day_2020_07(Day):

    def parse(self):
        parsed = dict()
        for rule in super().parse():
            splitted = rule.split(" ")
            bag_color = " ".join(splitted[:2])
            parsed[bag_color] = dict()
            if splitted[4] == "no":
                continue
            for i in range((len(splitted) - 4) // 4):
                quantity = int(splitted[4 + 4 * i])
                color = " ".join(splitted[4 + 4 * i + 1:4 + 4 * i + 3])
                parsed[bag_color][color] = quantity
        return parsed

    def bottom_up(self, search_color):
        search_color_parents = self.find_parents(search_color)
        queue = set(search_color_parents)
        found = set(search_color_parents)
        while len(queue) != 0:
            current_color = queue.pop()
            current_color_parents = self.find_parents(current_color)
            queue.update(current_color_parents)
            found.update(current_color_parents)
        return found

    def top_down(self, search_color):
        sum = 1
        for child_color in self.parsed[search_color]:
            sum += self.top_down(child_color) * self.parsed[search_color][child_color]
        return sum

    def find_parents(self, color):
        parents = list()
        for parent_color in self.parsed:
            if color in self.parsed[parent_color]:
                parents.append(parent_color)
        return parents

    def part_1(self):
        return len(self.bottom_up("shiny gold"))

    def part_2(self):
        return self.top_down("shiny gold") - 1


if __name__ == "__main__":
    Day_2020_07().solve()
