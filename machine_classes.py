class DFA:
    def __init__(self, states, alphabet, transitions, start, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start = start
        self.accept_states = accept_states

    def accepts(self, input_string):
        state = self.start
        for symbol in input_string:
            if (state, symbol) not in self.transitions:
                return False
            state = self.transitions[(state, symbol)]
        return state in self.accept_states
