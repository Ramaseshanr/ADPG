def is_string_accepted(transition_table:dict, initial_state:str, accepting_states:set, input_string:str) -> bool:
    """
    This function examines if a given string is accepted by a finite automaton.
    Parameters:
        transition_table: A dictionary stores (state, input_symbol) pairs and the next state
        initial_state: The starting state of the automaton
        accepting_states: A set of accepting states
        input_string: The input string to check.

    Returns:
        If the string is accepted, then it returns True, 
        else False
    """

    current_state = initial_state

    for symbol in input_string:
        next_state = transition_table.get((current_state, symbol))
        if next_state is None:  # No transition for the given input
            return False
        current_state = next_state

    #Checks if the current_state is a member of the accepted states
    return current_state in accepting_states

if __name__ == '__main__':

    # Language L is a set of strings formed over the alphabet {0,1}
    # A sample transition table - This accepts certain patterns of strings

    transition_table = {
        ('q0', '0'): 'q0',
        ('q0', '1'): 'q1',
        ('q1', '0'): 'q2',
        ('q1', '1'): 'q1',
        ('q2', '0'): 'q2',
        ('q2', '1'): 'q2'
    }

    initial_state = 'q0'
    # set of accepting states
    accepting_states = {'q2'}

    string = input('Input binary string: ')
    # string = '1010'
    # string = '0110'
    # string = '00010110000' Yes
    # string = '00010110100' No

    if is_string_accepted(transition_table, initial_state, accepting_states, string):
        print("The string is accepted.")
    else:
        print("The string is not accepted.")

