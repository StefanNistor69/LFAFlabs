from FiniteAutomaton import FiniteAutomaton
from Grammar import Grammars
class Main:

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

    def generate_strings(self, num_strings):
        for i in range(num_strings):
            string = self.grammar.generate_string()

            print(string)

if __name__ == '__main__':
    main = Main()
    main.generate_strings(5)
    automatons = main.grammar.to_finite_automaton()
    automaton = {
        'states': {'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
        'alphabet': {'a', 'b'},
        'transitions': {
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
    checker = FiniteAutomaton(automaton)
    checker.check_strings(['aaa', 'abaaa', 'ababaa', 'aa', 'abababa'])
    print(automatons)







