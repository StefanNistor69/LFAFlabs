import re


class Scanner:
    def __init__(self, productions):
        self.productions = productions
        self.start_symbol = 'S'

        # Extract all terminals from the productions
        self.terminals = set()
        for production in productions.values():
            if isinstance(production, list):
                for p in production:
                    # If production is a list, join its elements into a single string
                    # and extract terminals from it
                    self.terminals.update(re.findall(r'[a-z]', ''.join(p)))
            else:
                self.terminals.update(re.findall(r'[a-z]', production))

    def scan(self, input_string):
        tokens = []
        while input_string:
            matched = False
            # Sort the terminals in decreasing order of length, to match longer terminals first
            for terminal in sorted(self.terminals, key=lambda x: len(x), reverse=True):
                if input_string.startswith(terminal):
                    tokens.append(('TERMINAL', terminal))
                    input_string = input_string[len(terminal):]
                    matched = True
                    break

            if not matched:
                # If no terminal matches, raise an error
                raise ValueError('Invalid input')

        return tokens

