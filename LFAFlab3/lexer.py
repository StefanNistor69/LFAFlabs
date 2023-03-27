import re


class Lexer:
    # Initialize the lexer with the production rules
    def __init__(self, productions):
        self.productions = productions
        self.start_symbol = 'S'
        terminals = set()
        # Loop over the production rules to extract the terminals
        for value in productions.values():
            # If the production rule is a string, extract the lowercase letters
            if isinstance(value, str):
                terminals.update(re.findall(r'[a-z]', value))
            # If the production rule is a list of strings, join them together first and then extract the lowercase letters
            else:
                terminals.update(re.findall(r'[a-z]', ''.join(value)))
        self.terminals = terminals

    # Tokenize an input string
    def tokenize(self, input_string):
        tokens = []
        i = 0
        # Loop over the input string
        while i < len(input_string):
            # If the current character is a lowercase letter, it is a terminal symbol
            match = re.match(r'[a-z]', input_string[i])
            if match:
                tokens.append(('TERMINAL', match.group()))
                i += 1
            # If the current character is an uppercase letter, it is a non-terminal symbol
            else:
                match = re.match(r'[A-Z]', input_string[i])
                if match:
                    tokens.append(('NON_TERMINAL', match.group()))
                    i += 1
                # If the current character is neither a lowercase nor an uppercase letter, the input is invalid
                else:
                    raise ValueError('Invalid input')
        return tokens

