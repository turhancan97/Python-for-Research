#EXERCISE 2C

"""

The distance between two points x and y is the square root of the sum of s
quared differences along each dimension of x and y.
Create a function distance(x, y) that takes two vectors and outputs
the distance between them. Use your function to find the distance
between x=(0,0) and y=(1,1).
Print your answer.

"""

import math

def distance(x, y):
   # define your function here!
   
   
   return math.sqrt((y[1]-x[1])**2 + (y[0]-x[0])**2)

print(distance((0,0),(1,1)))
