#EXERCISE 2B

"""
Using random.uniform, create a function rand() that generates a single float
between -1 and 1.
Call rand() once. So we can check your solution, we will use random.seed
to fix the value called by your function.

"""


import random

random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.

def rand():
   # define `rand` here!
   
   return random.uniform(-1,1)

rand()
