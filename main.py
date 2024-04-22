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
    
# Define states, alphabet, transitions, start state, and accept states for the NFA

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
        (2, '_'): {3},


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
        (2, '_'): {3},

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
        (4, 'A'): {3},
        (4, 'B'): {3},
        (4, 'C'): {3},
        (4, 'D'): {3},
        (4, 'E'): {3},
        (4, 'F'): {3},
        (4, 'a'): {3},
        (4, 'b'): {3},
        (4, 'c'): {3},
        (4, 'd'): {3},
        (4, 'e'): {3},
        (4, 'f'): {3},
    }

    start_state = 0
    accept_state = {3}

class FloatingPointLiterals:
    states = {0,1,2,3,4,5,6,7,8,9,10,11,12}
    alphabet = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'e', 'E', '+', '-', '_'}
    transitions = {
        # (current_state, input_value): {next_state}
        (0, '0'): {1},
        (0, '1'): {1},
        (0, '2'): {1},
        (0, '3'): {1},
        (0, '4'): {1},
        (0, '5'): {1},
        (0, '6'): {1},
        (0, '7'): {1},
        (0, '8'): {1},
        (0, '9'): {1},
        (0, '.'): {9},

        (1, '0'): {1},
        (1, '1'): {1},
        (1, '2'): {1},
        (1, '3'): {1},
        (1, '4'): {1},
        (1, '5'): {1},
        (1, '6'): {1},
        (1, '7'): {1},
        (1, '8'): {1},
        (1, '9'): {1},
        (1, '_'): {2},
        (1, '.'): {3},
        (1, 'e'): {5},
        (1, 'E'): {5},


        (2, '0'): {1},
        (2, '1'): {1},
        (2, '2'): {1},
        (2, '3'): {1},
        (2, '4'): {1},
        (2, '5'): {1},
        (2, '6'): {1},
        (2, '7'): {1},
        (2, '8'): {1},
        (2, '9'): {1},

        (3, '0'): {4},
        (3, '1'): {4},
        (3, '2'): {4},
        (3, '3'): {4},
        (3, '4'): {4},
        (3, '5'): {4},
        (3, '6'): {4},
        (3, '7'): {4},
        (3, '8'): {4},
        (3, '9'): {4},
        (3, 'e'): {5},
        (3, 'E'): {5},

        (4, '0'): {4},
        (4, '1'): {4},
        (4, '2'): {4},
        (4, '3'): {4},
        (4, '4'): {4},
        (4, '5'): {4},
        (4, '6'): {4},
        (4, '7'): {4},
        (4, '8'): {4},
        (4, '9'): {4},
        (4, '_'): {12},
        (4, 'e'): {5},
        (4, 'E'): {5},

        (5, '0'): {6},
        (5, '1'): {6},
        (5, '2'): {6},
        (5, '3'): {6},
        (5, '4'): {6},
        (5, '5'): {6},
        (5, '6'): {6},
        (5, '7'): {6},
        (5, '8'): {6},
        (5, '9'): {6},
        (5, '+'): {8},
        (5, '-'): {8},

        (6, '0'): {6},
        (6, '1'): {6},
        (6, '2'): {6},
        (6, '3'): {6},
        (6, '4'): {6},
        (6, '5'): {6},
        (6, '6'): {6},
        (6, '7'): {6},
        (6, '8'): {6},
        (6, '9'): {6},
        (6, '_'): {7},

        (7, '0'): {6},
        (7, '1'): {6},
        (7, '2'): {6},
        (7, '3'): {6},
        (7, '4'): {6},
        (7, '5'): {6},
        (7, '6'): {6},
        (7, '7'): {6},
        (7, '8'): {6},
        (7, '9'): {6},

        (8, '0'): {6},
        (8, '1'): {6},
        (8, '2'): {6},
        (8, '3'): {6},
        (8, '4'): {6},
        (8, '5'): {6},
        (8, '6'): {6},
        (8, '7'): {6},
        (8, '8'): {6},
        (8, '9'): {6},


        (9, '0'): {10},
        (9, '1'): {10},
        (9, '2'): {10},
        (9, '3'): {10},
        (9, '4'): {10},
        (9, '5'): {10},
        (9, '6'): {10},
        (9, '7'): {10},
        (9, '8'): {10},
        (9, '9'): {10},

        (10, '0'): {10},
        (10, '1'): {10},
        (10, '2'): {10},
        (10, '3'): {10},
        (10, '4'): {10},
        (10, '5'): {10},
        (10, '6'): {10},
        (10, '7'): {10},
        (10, '8'): {10},
        (10, '9'): {10},
        (10, '_'): {11},
        (10, 'e'): {5},
        (10, 'E'): {5},

        (11, '0'): {10},
        (11, '1'): {10},
        (11, '2'): {10},
        (11, '3'): {10},
        (11, '4'): {10},
        (11, '5'): {10},
        (11, '6'): {10},
        (11, '7'): {10},
        (11, '8'): {10},
        (11, '9'): {10},

        (12, '0'): {3},
        (12, '1'): {3},
        (12, '2'): {3},
        (12, '3'): {3},
        (12, '4'): {3},
        (12, '5'): {3},
        (12, '6'): {3},
        (12, '7'): {3},
        (12, '8'): {3},
        (12, '9'): {3},

    }

    start_state = 0
    accept_state = {3, 4, 6, 10}

decimal_nfa = NFA(Decimal.states, Decimal.alphabet, Decimal.transitions, Decimal.start_state, Decimal.accept_state)

octal_nfa = NFA(Octal.states, Octal.alphabet, Octal.transitions, Octal.start_state, Octal.accept_state)

hex_nfa = NFA(Hexadecimal.states, Hexadecimal.alphabet, Hexadecimal.transitions, Hexadecimal.start_state, Hexadecimal.accept_state)

fpl_nfa = NFA(FloatingPointLiterals.states, FloatingPointLiterals.alphabet, FloatingPointLiterals.transitions, FloatingPointLiterals.start_state, FloatingPointLiterals.accept_state)

# for testing
test1 = ["0000", "0123", "23_23", "_23_23", "3__3", "33_2134_2342", "232423_", ".23e"]

test2 = [".0O2378", "0o_23", "0O13123"]

test3 = ["0xdeadbeef", "34", "0Xdede", "0xde_de0", "0x_ded", "0xdede_", "0xddada__da"]

test4 = [".01e", "1.e", "1.e34", "0.3", "3.14", "10.", ".001", "1e100", "3.14e-10", "0e0", "3.14_15_93", "0.23_", "0.23e+23912", "0.23e+2391_23_"]


# Check if the strings are recognized by the NFA

# for string in test1:
#     if decimal_nfa.is_accept(string):
#         print(f"'{string}' is valid .")
#     else:
#         print(f"'{string}' is not ")

# for string in test2:
#     if octal_nfa.is_accept(string):
#         print(f"'{string}' is a valid octal decimal number.")
#     else:
#         print(f"'{string}' is not a valid octal decimal number.")

# for string in test3:
#     if hex_nfa.is_accept(string):
#         print(f"'{string}' is valid .")
#     else:
#         print(f"'{string}' is not ")

# for string in test4:
#     if fpl_nfa.is_accept(string):
#         print(f"'{string}' is valid .")
#     else:
#         print(f"'{string}' is not ")


# main
user_input = input("Enter a number: ")
if decimal_nfa.is_accept(user_input):
    print(f"'{user_input}' is  a decimal integer!")

elif octal_nfa.is_accept(user_input):
    print(f"'{user_input}' is  an octal integer!")
   
elif hex_nfa.is_accept(user_input):
    print(f"'{user_input}' is  a hexadecimal integer!")

elif fpl_nfa.is_accept(user_input):
    print(f"'{user_input}' is floating  point literal!")

else:
    print("The input is not valid!")