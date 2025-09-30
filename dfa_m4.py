from machine_classes.dfa import DFA

# m4 accepts strings that start and end with the same character.

m4 = DFA(

    # states
    {'s', 'q1', 'q2', 'r1', 'r2'},

    # alphabet
    {'a', 'b'},

    # transition function
    {
        ('s', 'a'): 'q1',
        ('s', 'b'): 'r1',

        ('q1', 'a'): 'q1',
        ('q1', 'b'): 'q2',
        ('q2', 'b'): 'q2',
        ('q2', 'a'): 'q1',

        ('r1', 'b'): 'r1',
        ('r1', 'a'): 'r2',
        ('r2', 'a'): 'r2',
        ('r2', 'b'): 'r1'
    },

    # start state
    's',

    # accept states
    {'q1', 'r1'}
)
