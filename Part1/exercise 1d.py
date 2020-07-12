"""

Abraham Lincoln was a president during the American Civil War.
His famous 1863 Gettysburg Address has been stored as address,
and the counter function defined in part 1c has been loaded.
Use these to return a dictionary consisting of the count of each
letter in this address, and save this as address_count.
Print address_count.

"""

from func import counter #imports counter function, previously made and saved as func.py
from string import ascii_letters

address_count = {}

with open("address.txt") as f:

    address = [line.rstrip('\n') for line in f]

count = 0

while count < len(address):

    taddress_count = counter(address[count])

    for key in taddress_count.keys():

        if key in address_count.keys():

            taddress_count[key] += address_count[key]
        
    count += 1
    address_count.update(taddress_count)

print(address_count)


#EXERCISE 1E

"""

The frequency of each letter in the Gettysburg Address is already stored
as address_count. Use this dictionary to find the most common letter in
the Gettysburg address.
Store this letter as most_frequent_letter, and print your answer.

"""

alphabet = ascii_letters

alphapos = 0

most_frequent_letter = ''

most_frequent = 0

while alphapos < len(alphabet):


    if alphabet[alphapos] in address_count.keys():

    

        number = address_count[alphabet[alphapos]]

                

        if number > most_frequent:

            most_frequent = number

            alphapos += 1

        else:

            alphapos += 1

    else:

        number = 0

        alphapos += 1
        
for letter, count in address_count.items():

    if count == most_frequent:

        most_frequent_letter = letter

print (most_frequent_letter)

