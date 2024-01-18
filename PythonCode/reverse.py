def string_len(input_string:str) -> int:
    '''
    return the length of the string
    input: a string
    '''
    #initialize the counter
    count = 0

    # Loop until we exhausted the input string
    for i in input_string:
        #increment the counter
        count += 1

    #return the length of the string
    return count

def reverse_string(input_string:str) -> str:
    '''
    Return the reverse of the input_string
    '''
    # get the length of the input string before the loop as this is a constant for a given string length
    len = string_len(input_string)

    # initialize the counter to -1 as we are going to read from the last character
    i = -1

    # store the result in the output_str variable
    output_string = ''

    while input_string[i] != None:
        output_string += input_string[i]
        i -= 1

        #Check if we have read all the charaters in the input string
        if i*(-1) > len:
            break

    return output_string

if __name__ == '__main__':
    #get the input string
    input_string = input('Input a string: ')

    # print the output string
    print(reverse_string(input_string))    
