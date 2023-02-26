import random

class Grammars:
    def __init__(self, productions, start_symbol):
        # Initialize the class with a dictionary of productions and a start symbol
        self.productions = productions
        self.start_symbol = start_symbol

    def generate_string(self):
        # Generate a string from the start symbol using the internal recursive method
        return self._generate_string(self.start_symbol)

    def _generate_string(self, symbol):
        # If the current symbol is a terminal symbol, return it
        if symbol not in self.productions:
            return symbol
        # Otherwise, choose a random production for the current symbol and recursively generate a string from each symbol in the production
        production = random.choice(self.productions[symbol])
        return ''.join(self._generate_string(s) for s in production)


    def to_finite_automaton(self):
        # Initialize the finite automaton with a start state
        start_state = 0
        automatons = {start_state: {}}
        state_count = 1

        # Iterate over each symbol in the productions dictionary
        for symbol in self.productions:
            # Iterate over each production for the current symbol
            for production in self.productions[symbol]:
                current_state = start_state
                # For each symbol in the production, create a new state if necessary and add a transition to the finite automaton
                for s in production:
                    if s not in automatons[current_state]:
                        automatons[current_state][s] = state_count
                        automatons[state_count] = {}
                        state_count += 1
                    current_state = automatons[current_state][s]
                # Add an epsilon transition from the final state of the production to the start state of the finite automaton
                if current_state not in automatons:
                    automatons[current_state] = {}
                automatons[current_state][''] = start_state

        # Return the resulting finite automaton
        return automatons

