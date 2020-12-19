
from common import Day
import itertools


class Day_2020_19(Day):

    def parse(self):
        parts = self.input.split("\n\n")
        rules = parts[0].split("\n")
        self.rules = [None] * len(rules)
        self.expanded_rules = [None] * len(rules)
        self.messages = set(parts[1].split("\n"))
        for rule in rules:
            rule = rule.split(": ")
            rule_id = int(rule[0])
            rule_value = rule[1]
            if rule_value[0] == '"':
                self.expanded_rules[rule_id] = rule_value[1]
            else:
                self.rules[rule_id] = list()
                for rule_part in rule_value.split(" | "):
                    self.rules[rule_id].append([int(x) for x in rule_part.split(" ")])

    def expand_rule(self, rule_id):
        if self.expanded_rules[rule_id]:
            return self.expanded_rules[rule_id]
        self.expanded_rules[rule_id] = []
        for sub_rule in self.rules[rule_id]:
            values = [self.expand_rule(id) for id in sub_rule]
            product = list(itertools.product(*values))
            self.expanded_rules[rule_id] += ["".join(x) for x in product]
        return self.expanded_rules[rule_id]

    def part_1(self):
        possible_messages = self.expand_rule(0)
        return None

    def part_2(self):
        return None


if __name__ == "__main__":
    Day_2020_19().solve()
