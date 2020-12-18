
from common import Day


class Day_2020_18(Day):

    class Tree:

        root = None

        class Node:
            value = None
            left = None
            right = None

            def __init__(self, value, left, right):
                self.value = value
                self.left = left
                self.right = right

        def __init__(self, string, precedences=None):
            precedences = precedences or {"+": 0, "-": 0, "*": 1, "/": 1, "**": 2}
            tokens = self.tokenize(string)
            self.root = self.parse(tokens, precedences)

        def tokenize(self, string):
            return string.replace("(", "( ").replace(")", " )").split(" ")

        def parse(self, tokens, precedences):
            operators = []
            operands = []
            for token in tokens:
                if token.isnumeric():
                    operands.append(self.Node(int(token), None, None))
                elif token == "(":
                    operators.append(token)
                elif token == ")":
                    while len(operators) > 0 and operators[-1] != '(':
                        right = operands.pop()
                        op = operators.pop()
                        left = operands.pop()
                        operands.append(self.Node(op, left, right))
                    operators.pop()
                elif len(operators) > 0 and operators[-1] != "(" and precedences[token] <= precedences[operators[-1]]:
                    right = operands.pop()
                    op = operators.pop()
                    left = operands.pop()
                    operands.append(self.Node(op, left, right))
                    operators.append(token)
                else:
                    operators.append(token)
            while len(operators) > 0:
                right = operands.pop()
                op = operators.pop()
                left = operands.pop()
                operands.append(self.Node(op, left, right))
            return operands.pop()

        def evaluate(self, node=None):
            node = node or self.root
            if type(node.value) == int:
                return node.value
            else:
                if node.value == "+":
                    return self.evaluate(node.left) + self.evaluate(node.right)
                elif node.value == "-":
                    return self.evaluate(node.left) - self.evaluate(node.right)
                elif node.value == "*":
                    return self.evaluate(node.left) * self.evaluate(node.right)
                elif node.value == "/":
                    return self.evaluate(node.left) / self.evaluate(node.right)
                elif node.value == "**":
                    return self.evaluate(node.left) ** self.evaluate(node.right)

    def part_1(self):
        precedences = {"+": 0, "-": 0, "*": 0, "/": 0, "**": 0}
        return sum(self.Tree(query, precedences).evaluate() for query in self.parsed)

    def part_2(self):
        precedences = {"+": 1, "-": 1, "*": 0, "/": 0, "**": 0}
        return sum(self.Tree(query, precedences).evaluate() for query in self.parsed)


if __name__ == "__main__":
    Day_2020_18().solve()
