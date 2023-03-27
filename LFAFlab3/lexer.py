import re


class Lexer:
    def __init__(self, productions):
        self.productions = productions
        self.start_symbol = 'S'
        self.terminals = set(re.findall(r'[a-z]', ''.join(productions.values())))

    def tokenize(self, input_string):
        tokens = []
        i = 0
        while i < len(input_string):
            match = re.match(r'[a-z]', input_string[i])
            if match:
                tokens.append(('TERMINAL', match.group()))
                i += 1
            else:
                match = re.match(r'[A-Z]', input_string[i])
                if match:
                    tokens.append(('NON_TERMINAL', match.group()))
                    i += 1
                else:
                    raise ValueError('Invalid input')
        return tokens
