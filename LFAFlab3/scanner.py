import re

class Scanner:
    def __init__(self, productions):
        self.productions = productions
        self.start_symbol = 'S'
        self.terminals = set(re.findall(r'[a-z]', ''.join(productions.values())))

    def scan(self, input_string):
        tokens = self.tokenize(input_string)
        stack = [self.start_symbol]
        i = 0
        while stack:
            current = stack.pop()
            if current in self.terminals:
                if i < len(tokens) and tokens[i][1] == current:
                    i += 1
                else:
                    raise ValueError('Invalid input')
            elif current in self.productions:
                for production in self.productions[current]:
                    stack += list(production)[::-1]
            else:
                raise ValueError('Invalid grammar')
        if i != len(tokens):
            raise ValueError('Invalid input')
