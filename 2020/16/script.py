
from common import Day


class Day_2020_16(Day):

    def parse(self):
        self.rules = dict()
        self.tickets = list()
        parts = self.input.split("\n\n")
        rules = parts[0].split("\n")
        my_ticket = parts[1].split("\n")[1:]
        nearby_tickets = parts[2].split("\n")[1:]
        for rule in rules:
            rule = rule.split(": ")
            self.rules[rule[0]] = list()
            rule_values = rule[1].split(" or ")
            for rule_value in rule_values:
                rule_value = [int(x) for x in rule_value.split("-")]
                self.rules[rule[0]].append(range(rule_value[0], rule_value[1] + 1))
        for ticket in my_ticket + nearby_tickets:
            self.tickets.append([int(x) for x in ticket.split(",")])

    def get_valid_tickets(self):
        valid_tickets = []
        for ticket in self.tickets:
            if self.ticket_is_valid(ticket):
                valid_tickets.append(ticket)
        return valid_tickets

    def ticket_is_valid(self, ticket):
        for value in ticket:
            if not self.value_is_valid_for_any_rule(value):
                return False
        return True

    def value_is_valid_for_any_rule(self, value):
        for rule_name in self.rules:
            if self.value_is_valid_for_rule(value, rule_name):
                return True
        return False

    def value_is_valid_for_rule(self, value, rule_name):
        for value_range in self.rules[rule_name]:
            if value in value_range:
                return True
        return False

    def rule_is_valid_for_ticket_values(self, index, rule_name):
        for value in [values[index] for values in self.tickets]:
            if not self.value_is_valid_for_rule(value, rule_name):
                return False
        return True

    def get_valid_rules_graph(self):
        valid_rules_graph = dict()
        for i in range(len(self.tickets[0])):
            valid_rules_graph[i] = set()
            for rule_name in self.rules:
                if self.rule_is_valid_for_ticket_values(i, rule_name):
                    valid_rules_graph[i].add(rule_name)
        return valid_rules_graph

    def get_map(self):
        determined_rules = set()
        map = dict()
        valid_rules_graph = self.get_valid_rules_graph()
        for index in sorted(valid_rules_graph, key=lambda index: len(valid_rules_graph[index]), reverse=False):
            valid_rules = valid_rules_graph[index] - determined_rules
            if len(valid_rules) != 1:
                raise Exception()
            else:
                rule = valid_rules.pop()
                determined_rules.add(rule)
                map[index] = rule
        return map

    def part_1(self):
        error_rate = 0
        for ticket in self.tickets[1:]:
            for value in ticket:
                if not self.value_is_valid_for_any_rule(value):
                    error_rate += value
        return error_rate

    def part_2(self):
        product = 1
        self.tickets = self.get_valid_tickets()
        for index, rule_name in self.get_map().items():
            if rule_name.startswith("departure "):
                product *= self.tickets[0][index]
        return product


if __name__ == "__main__":
    Day_2020_16().solve()
