import re

class Lexer:
    def __init__(self):
        self.tokens = []
        self.terminal_pattern = re.compile(r"\s*([-+\/*()])")
        self.nonterminal_pattern = re.compile(r"\s*([a-zA-Z]+|[0-9]+)")

    def tokenize(self, input_string):
        while len(input_string) > 0:
            match = self.terminal_pattern.match(input_string)
            if match:
                token = ("TERMINAL", match.group(0))
                self.tokens.append(token)
                input_string = input_string[len(token[1]):]
            else:
                match = self.nonterminal_pattern.match(input_string)
                if not match:
                    raise ValueError(f"Invalid token: {input_string}")
                token = ("NON-TERMINAL", match.group(0))
                self.tokens.append(token)
                input_string = input_string[len(token[1]):]
        return self.tokens
