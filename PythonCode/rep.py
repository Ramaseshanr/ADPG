def quirky_replacement(input_string:str, 
                       vowels:str='aeiou', 
                       consonants:str='bcdfghjklmnpqrstvwxz') -> str:
    '''
    This quirky version where vowels are replaced with consonants. 
    If English vowels and consonants were used as input variables, the the 
    first vowel gets swapped with the first consonant, the second vowel 
    with the second consonant, and so on

    input_string -> contains the string to be transformed
    vowels:str -> stores the vovwels
    consonants:str -> stores the consonants
    Returns the transformed string
    '''
    new_sentence = ''
    Found = False

    # The enumerate function yields a pair of values.
    # Each pair (index,value) represents the index of the of the object (in this case a character) and its value
    # The first pair in this example is (0,'t')
    # The second pair is (1,'h') and so on

    for i, char in enumerate(input_string):
        for j in range(len(vowels)):
            found = False
            if vowels[j] == char:
                found = True
                break
        if  found == False:
            new_sentence += char
        else:
            new_sentence += consonants[j]

    return new_sentence

if __name__ == '__main__':
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxz'
    sentence = 'the quick brown fox jumped over the lazy dog' 

    transformed_sentence = quirky_replacement(sentence, vowels=vowels, consonants=consonants)
    print(transformed_sentence)

    #the above two statements can be replaced by the following
    print(quirky_replacement(sentence))