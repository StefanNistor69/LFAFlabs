
class FiniteAutomaton:
    def __init__(self, automaton):
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5'}
        # self.states = automaton['states']
        self.alphabet = {'a', 'b'}
        self.transitions = {
            'q0': {'a': 'q1'},
            'q1': {'b': 'q2', 'a': 'q3'},
            'q2': {'a': 'q4'},
            'q3': {'a': 'q1', 'b': 'q5'},
            'q4': {'a': 'q5', 'b': 'q5'},
            'q5': {'a': 'q5', 'b': 'q5'}
        }
        self.start_state = {'q0'}
        self.final_states = {'q5'}

    def check_string(self, string):

        current_state = self.start_state

        for symbol in string:
            try:
                current_state = self.transitions[current_state][symbol]
            except KeyError:
                return False

        return current_state in self.final_states

    def check_strings(self, strings):

        for string in strings:
            if self.check_string(string):
                print(f'String "{string}" is accepted by the automaton.')
            else:
                print(f'String "{string}" is rejected by the automaton.')