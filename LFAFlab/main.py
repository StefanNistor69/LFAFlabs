import string

from FiniteAutomaton import FiniteAutomaton
from Grammar import Grammars
class Main:
    # Initialize the Main class by setting up a grammar,
    # converting it to a finite automaton, and setting up a FiniteAutomaton object
    def __init__(self):
        self.productions = {
            'S': ['aA', 'aB'],
            'A': ['bS'],
            'B': ['aC'],
            'C': ['a', 'bS'],
        }
        self.start_symbol = 'S'
        self.grammar = Grammars(self.productions, self.start_symbol)
        self.finite_automaton = self.grammar.to_finite_automaton()
        self.automaton = FiniteAutomaton

    # Generates strings from the grammar
    def generate_strings(self, num_strings):
        for i in range(num_strings):
            string = self.grammar.generate_string()
            print(string)

if __name__ == '__main__':
    # Create a Main object
    main = Main()

    # Generate and print 5 strings from the grammar
    main.generate_strings(5)

    # Convert the grammar to a finite automaton
    automatons = main.grammar.to_finite_automaton()

    # Define a finite automaton manually
    automaton = {
        'states': {'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
        'alphabet': {'a', 'b'},
        'transition': {
            'q0': {'a': 'q1'},
            'q1': {'b': 'q2', 'a': 'q3'},
            'q2': {'a': 'q4'},
            'q3': {'a': 'q1', 'b': 'q5'},
            'q4': {'a': 'q5', 'b': 'q5'},
            'q5': {'a': 'q5', 'b': 'q5'}
        },
        'start_state': 'q0',
        'final_states': {'q5'}
    }

    # Create a FiniteAutomaton object for the manually-defined automaton
    checker = FiniteAutomaton(automaton)

    # Check whether a list of strings are accepted by the finite automaton
    checker.check_strings(['aaa', 'abaaa', 'ababaa', 'aa', 'abababa'])

    # Print the finite automaton
    print(automatons)







