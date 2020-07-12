"""

Rewrite your code from 1b to make a function called counter that takes a string
input_string and returns a dictionary of letter counts count_letters.
If you were unable to complete 1b, you can use the solution by selecting

Show Answer.
Use your function to call counter(sentence).

"""

from string import ascii_letters #imports ascii_letter from string library

sentence = 'Jim quickly realized that the beautiful gowns are expensive'


def counter(sentence):

    alphabet = ascii_letters

    count_letters = {}

    for letter in sentence: #check whether each letter in the sentence is in the alphabet
        
        if letter in alphabet:
            
            if letter in count_letters: #if in alphabet, check whether it is in the count_letter dictionary
                
                count_letters[letter] += 1 #if so, increment its count value by 1

            else:
                
                count_letters[letter] = 1 #if not, set its value to 1

    return count_letters #return count_letters dictionary


print(counter(sentence))
