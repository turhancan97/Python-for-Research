from string import ascii_letters

def counter(sentence):

    alphabet = ascii_letters

    count_letters = {}

    for letter in sentence:
        
        if letter in alphabet:
            
            if letter in count_letters:
                
                count_letters[letter] += 1

            else:
                
                count_letters[letter] = 1

    return count_letters
