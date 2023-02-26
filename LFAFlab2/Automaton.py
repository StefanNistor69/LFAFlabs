class Automaton:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3'}
        self.alphabet = {'a', 'b', 'c'}
        self.start_state = 'q0'
        self.accept_states = {'q3'}
        self.transitions = {
            ('q0', 'a'): {'q0', 'q1'},
            ('q1', 'b'): {'q2'},
            ('q2', 'a'): {'q2'},
            ('q3', 'a'): {'q3'},
            ('q2', 'b'): {'q3'}
        }

    def is_deterministic(self):
        for state in self.states:
            for symbol in self.alphabet:
                next_states = self.transitions.get((state, symbol), set())
                if len(next_states) != 1:
                    return False
        return True

    def to_dfa(self):
        if self.is_deterministic():
            return self

        dfa_states = set()
        dfa_accept_states = set()
        dfa_transitions = dict()
        state_queue = [frozenset([self.start_state])]
        while state_queue:
            current_states = state_queue.pop(0)
            dfa_states.add(current_states)
            if any(state in self.accept_states for state in current_states):
                dfa_accept_states.add(current_states)
            for symbol in self.alphabet:
                next_states = set()
                for state in current_states:
                    next_states |= set(self.transitions.get((state, symbol), set()))
                if next_states:
                    next_states = frozenset(next_states)
                    dfa_transitions[(current_states, symbol)] = next_states
                    if next_states not in dfa_states:
                        state_queue.append(next_states)

        dfa = Automaton()
        dfa.states = dfa_states
        dfa.accept_states = dfa_accept_states
        dfa.transitions = dfa_transitions
        return dfa

    def to_grammar(self):
        productions = dict()
        for state in self.states:
            for symbol in self.alphabet:
                next_states = self.transitions.get((state, symbol), set())
                for next_state in next_states:
                    if next_state in self.accept_states:
                        if state not in productions:
                            productions[state] = set()
                        productions[state].add(symbol)
                    else:
                        if next_state not in productions:
                            productions[next_state] = set()
                        productions[next_state].add(symbol + state)
        start_symbol = self.start_state
        if start_symbol in productions:
            productions['S'] = productions[start_symbol]
            del productions[start_symbol]
            for state in self.states:
                for symbol in self.alphabet:
                    next_states = self.transitions.get((state, symbol), set())
                    for next_state in next_states:
                        if state in productions and symbol + state in productions[state]:
                            if next_state not in productions:
                                productions[next_state] = set()
                            productions[next_state].add(symbol + 'S')
        else:
            start_symbol = 'S'
            productions[start_symbol] = set()
            for accept_state in self.accept_states:
                productions[start_symbol].add('eps' + accept_state)

        return start_symbol, productions
