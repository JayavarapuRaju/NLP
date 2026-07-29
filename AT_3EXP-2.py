# DFA Simulator for Strings Ending with "ab"

# Transition Table
transition = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': 'q1', 'b': 'q2'},
    'q2': {'a': 'q1', 'b': 'q0'}
}

# DFA Details
initial_state = 'q0'
final_states = ['q2']

# Number of input strings
n = int(input("Enter number of input strings: "))

for i in range(n):
    string = input(f"\nEnter String {i+1}: ")

    current_state = initial_state
    path = [current_state]

    valid = True

    # Simulate DFA
    for symbol in string:
        if symbol not in ['a', 'b']:
            valid = False
            break
        current_state = transition[current_state][symbol]
        path.append(current_state)

    # Output
    print("Transition Path:")
    print(" → ".join(path))

    if valid and current_state in final_states:
        print("Accepted")
    else:
        print("Rejected")
