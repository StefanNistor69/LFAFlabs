from FiniteAutomaton import FiniteAutomaton
from Grammar import Grammars
class Main:

    def __init__(self):
        self.productions = {
            'S': ['dA'],
            'A': ['d', 'aB'],
            'B': ['bC'],
            'C': ['cA', 'aS'],
        }
        self.start_symbol = 'S'
        self.grammar = Grammars(self.productions, self.start_symbol)
        self.finite_automaton = self.grammar.to_finite_automaton()
        self.automaton = FiniteAutomaton

    def generate_strings(self, num_strings):
        for i in range(num_strings):
            string = self.grammar.generate_string()

            print(string)

if __name__ == '__main__':
    main = Main()
    main.generate_strings(5)
    automatons = main.grammar.to_finite_automaton()
    automaton = {
        'states': {'q0', 'q1', 'q2', 'q3', 'q4'},
        'alphabet': {'a', 'b', 'c', 'd'},
        'transitions': {
            'q0': {'d': 'q1'},
            'q1': {'d': 'q2', 'a': 'q3'},
            'q2': {'b': 'q4'},
            'q3': {'c': 'q0', 'a': 'q1'},
            'q4': {'a': 'q1'}
        },
        'start_state': 'q0',
        'final_states': {'q1'}
    }
    checker = FiniteAutomaton(automaton)
    checker.check_strings(['daac', 'daad', 'daa', 'aa', 'dacada'])
    print(automatons)







