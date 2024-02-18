from operator import add, sub, mul, truediv, mod
from re import findall


def tokenize(expression):
    return findall(r'[-+*/%=()]|[\w.]+', expression)


class Interpreter:
    OPERATORS = {'+': add, '-': sub, '*': mul, '/': truediv, '%': mod}

    def __init__(self):
        self.variables = {}

    def input(self, expression):
        tokens = tokenize(expression)
        if '=' in tokens:
            value = self.evaluate_expression(tokens[2:])
            self.variables[tokens[0]] = value
            return value
        return self.evaluate_expression(tokens)

    def parse(self, item):
        return float(self.variables.get(item, item))

    def evaluate_expression(self, tokens):
        if not tokens:
            return ''

        while '(' in tokens:
            opened = closed = 0
            i = tokens.index('(')
            for j, tok in enumerate(tokens):
                if tok == '(':
                    opened += 1
                elif tok == ')':
                    closed += 1
                if opened and opened == closed:
                    tokens[i:j + 1] = [self.evaluate_expression(tokens[i + 1:j])]
                    break

        for operators_set in ({'*', '/', '%'}, {'+', '-'}):
            i = 1
            while i < len(tokens):
                if tokens[i] in operators_set:
                    left, right = map(self.parse, (tokens[i - 1], tokens[i + 1]))
                    tokens[i - 1:i + 2] = [self.OPERATORS[tokens[i]](left, right)]
                else:
                    i += 2

        if len(tokens) != 1:
            raise ValueError

        return self.parse(tokens.pop())
