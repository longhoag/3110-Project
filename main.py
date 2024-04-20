# this is going to simulate the NFA design we have
class NFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def is_accept(self, string):
        current_states = {self.start_state}
        for char in string:
            next_states = set()
            for state in current_states:
                if (state, char) in self.transitions:
                    next_states |= self.transitions[(state, char)]
            current_states = next_states
        return bool(current_states & self.accept_states)
    
class Decimal:
    states = {0,1,2,3,4}
    alphabet = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_'}
    transitions = {
        # (current_state, input_value): {next_state}
        (0, '0'): {1},

        (0, '1'): {3},
        (0, '2'): {3},
        (0, '3'): {3},
        (0, '4'): {3},
        (0, '5'): {3},
        (0, '6'): {3},
        (0, '7'): {3},
        (0, '8'): {3},
        (0, '9'): {3},

        (1, '0'): {1},
        (1, '_'): {2},

        (2, '0'): {1},

        (3, '0'): {3},
        (3, '1'): {3},
        (3, '2'): {3},
        (3, '3'): {3},
        (3, '4'): {3},
        (3, '5'): {3},
        (3, '6'): {3},
        (3, '7'): {3},
        (3, '8'): {3},
        (3, '9'): {3},
        (3, '_'): {4},

        (4, '0'): {3},
        (4, '1'): {3},
        (4, '2'): {3},
        (4, '3'): {3},
        (4, '4'): {3},
        (4, '5'): {3},
        (4, '6'): {3},
        (4, '7'): {3},
        (4, '8'): {3},
        (4, '9'): {3},
    }

    start_state = 0
    accept_state = {1, 3}

# Define states, alphabet, transitions, start state, and accept states for the octal decimal NFA
class Octal:
    states = {0,1,2,3,4}
    alphabet = {'0', '1', '2', '3', '4', '5', '6', '7', 'o', 'O', '_'}
    transitions = {
        # (current_state, input_value): {next_state}
        (0, '0'): {1},

        (1, 'o'): {2},
        (1, 'O'): {2},

        (2, '0'): {3},
        (2, '1'): {3},
        (2, '2'): {3},
        (2, '3'): {3},
        (2, '4'): {3},
        (2, '5'): {3},
        (2, '6'): {3},
        (2, '7'): {3},
        (3, '0'): {3},
        (3, '1'): {3},
        (3, '2'): {3},
        (3, '3'): {3},
        (3, '4'): {3},
        (3, '5'): {3},
        (3, '6'): {3},
        (3, '7'): {3},
        (3, '_'): {4},
        (4, '0'): {3},
        (4, '1'): {3},
        (4, '2'): {3},
        (4, '3'): {3},
        (4, '4'): {3},
        (4, '5'): {3},
        (4, '6'): {3},
        (4, '7'): {3},
    }

    start_state = 0
    accept_state = {3}

class Hexadecimal:
    states = {0,1,2,3,4}
    alphabet = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f', '_'}
    transitions = {
        # (current_state, input_value): {next_state}
        (0, '0'): {1},

        (1, 'x'): {2},
        (1, 'X'): {2},

        (2, '0'): {3},
        (2, '1'): {3},
        (2, '2'): {3},
        (2, '3'): {3},
        (2, '4'): {3},
        (2, '5'): {3},
        (2, '6'): {3},
        (2, '7'): {3},
        (2, '8'): {3},
        (2, '9'): {3},
        (2, 'A'): {3},
        (2, 'B'): {3},
        (2, 'C'): {3},
        (2, 'D'): {3},
        (2, 'E'): {3},
        (2, 'F'): {3},
        (2, 'a'): {3},
        (2, 'b'): {3},
        (2, 'c'): {3},
        (2, 'd'): {3},
        (2, 'e'): {3},
        (2, 'f'): {3},

        (3, '0'): {3},
        (3, '1'): {3},
        (3, '2'): {3},
        (3, '3'): {3},
        (3, '4'): {3},
        (3, '5'): {3},
        (3, '6'): {3},
        (3, '7'): {3},
        (3, '8'): {3},
        (3, '9'): {3},
        (3, 'A'): {3},
        (3, 'B'): {3},
        (3, 'C'): {3},
        (3, 'D'): {3},
        (3, 'E'): {3},
        (3, 'F'): {3},
        (3, 'a'): {3},
        (3, 'b'): {3},
        (3, 'c'): {3},
        (3, 'd'): {3},
        (3, 'e'): {3},
        (3, 'f'): {3},
        (3, '_'): {4},


        (4, '0'): {3},
        (4, '1'): {3},
        (4, '2'): {3},
        (4, '3'): {3},
        (4, '4'): {3},
        (4, '5'): {3},
        (4, '6'): {3},
        (4, '7'): {3},
        (4, '8'): {3},
        (4, '9'): {3},
    }

    start_state = 0
    accept_state = {1, 3}

decimal_nfa = NFA(Decimal.states, Decimal.alphabet, Decimal.transitions, Decimal.start_state, Decimal.accept_state)

octal_nfa = NFA(Octal.states, Octal.alphabet, Octal.transitions, Octal.start_state, Octal.accept_state)

test2 = [".0O2378", "0o_23", "0O13123"]

test1 = ["0000", "0123", "23_23", "_23_23", "3__3", "33_2134_2342", "232423_", ".23e"]

# Check if the strings are recognized by the NFA

for string in test1:
    if decimal_nfa.is_accept(string):
        print(f"'{string}' is a valid  decimal number.")
    else:
        print(f"'{string}' is not a valid  decimal number.")


# for string in test:
#     if octal_nfa.is_accept(string):
#         print(f"'{string}' is a valid octal decimal number.")
#     else:
#         print(f"'{string}' is not a valid octal decimal number.")