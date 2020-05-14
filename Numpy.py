# Numpy

import numpy as np

zero_vector = np.zeros(5)
zero_matrix = np.zeros((3,5))
print(zero_vector)
print(zero_matrix)

x = np.array([1,2,3])
y = np.array([2,4,6])
print(y)
print(x)

print(np.array([[1,3],[5,9]]))

A = np.array([[1,3],[5,9]])
print(A.transpose())
print("------------------------")
# Slicing Numpy Arrays

x = np.array([1,2,3])
y = np.array([2,4,6])
X = np.array([[1,2,3],[4,5,6]])
Y = np.array([[2,4,6],[8,10,12]])

print(x[2])
print(x[0:2])
z = x + y
print(z)
print(X[:,1])
print(Y[:,1])
print(X[:,1]+Y[:,1])
print(X[1,:])

print(np.array([2,4]) + np.array([6,8]))
print("------------------------")
# Indexing Numpy Arrays

z1 = np.array([1,3,5,7,9])
z2 = z1 + 1
print(z2)
ind = [0,2,3]
print(z1[ind])
z1 = np.array([1,3,5,7,9])
print(z>6)
print(z1[z1>6])
print(z2[z1>6])
w = z1[0:3]
print(w)
w[0] = 3
print(w)
print(z1)
z1 = np.array([1,3,5,7,9])
ind = np.array([0,1,2])
w = z1[ind]
print(w)
w[0] = 3
print(z1)
print(w)
print("------------------------")
# Building and Examining NumPy Arrays
q = np.linspace(0,100,10)
print("\n",q)
e = np.logspace(1,2,10)
print("\n",e)
t = np.logspace(np.log10(250),np.log10(500),10)
print("\n",t)
X = np.array([[1,2,3],[4,5,6]])
print("\n",X.shape)
print("\n",X.size)
x = np.random.random(10)
print(np.any(x > 0.9))
print(np.all(x>=0.1))
print(x)