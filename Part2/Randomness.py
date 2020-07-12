#Simulating Randomness

import random
random.choice(["H","T"])
random.choice([0,1])
random.choice([0,1,2,3,4,5,6])
random.choice(range(1,7))
random.choice([range(1,7),range(1,9),range(1,11)])
random.choice(random.choice([range(1,7),range(1,9),range(1,11)]))

#Examples Involving Randomness

import matplotlib.pyplot as plt
import numpy as np
rolls = []
for k in range(100):
   rolls.append(random.choice([1,2,3,4,5,6]))
   
rolls
plt.hist(rolls,bins=np.linspace(0.5,6.5,7))

ys = []
for rep in range (1000):
    y=0
    for k in range(10):
        x = random.choice([1,2,3,4,5,6])
        y = y + x
    ys.append(y)
ys
plt.hist(ys)

#Using the NumPy Random Module

np.random.random()
np.random.random(5)
np.random.random((5,3))
np.random.normal(0,1)
np.random.normal(0,1,5)
np.random.normal(0,1,(2,2))
np.random.randint(1,7)

X = np.random.randint(1,7,(100,10))
np.sum(X)
np.sum(X,axis=1)
Y = np.sum(X,axis=1)
plt.hist(Y)

np.sum(np.random.randint(1,7,(100,10)), axis=0)


#Measuring Time

import time
start_time = time.clock()
ys = []
for rep in range (1000):
    y=0
    for k in range(10):
        x = random.choice([1,2,3,4,5,6])
        y = y + x
    ys.append(y)
end_time = time.clock()
print(end_time-start_time)

start_time2 = time.clock()
X = np.random.randint(1,7,(1000,10))
np.sum(X)
np.sum(X,axis=1)
Y = np.sum(X,axis=1)
end_time2 = time.clock()
print(end_time2 - start_time2)

#Random Walks

delta_X = np.random.normal(0,1,(2,10000))
plt.plot(delta_X[0],delta_X[1],"go")
X = np.cumsum(delta_X,axis=1)
X
plt.plot(X[0],X[1],"ro-")
X_0 = np.array([[0],[0]])
Z = np.concatenate((X_0,X),axis=1)
Z
plt.plot(Z[0],Z[1],"ro-")
