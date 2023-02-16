
import random

class Grammars:
    def __init__(self, productions, start_symbol):
        self.productions = productions
        self.start_symbol = start_symbol

    def generate_string(self):
        return self._generate_string(self.start_symbol)

    def _generate_string(self, symbol):
        if symbol not in self.productions:
            return symbol
        production = random.choice(self.productions[symbol])
        return ''.join(self._generate_string(s) for s in production)

    def to_finite_automaton(self):
        # Initialize the automaton with a single start state
        start_state = 0
        automatons = {start_state: {}}
        state_count = 1

        # Add transitions for each production rule
        for symbol in self.productions:
            for production in self.productions[symbol]:
                current_state = start_state
                for s in production:
                    if s not in automatons[current_state]:
                        # Add a new state and transition
                        automatons[current_state][s] = state_count
                        automatons[state_count] = {}
                        state_count += 1
                    current_state = automatons[current_state][s]
                # Add an epsilon transition to the final state for the last symbol in the production
                if current_state not in automatons:
                    automatons[current_state] = {}
                automatons[current_state][''] = start_state

        # Return the automaton
        return automatons

