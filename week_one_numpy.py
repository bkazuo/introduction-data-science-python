import numpy as np # If it does not exist, sudo apt install python-pip

# Create a list and convert it to a numpy array
mylist = [1, 2, 3]
x = np.array(mylist)
print(x)
print("---------------")

# Pass in a list of lists to create a multidimensional array
m = np.array([[7,8,9], [10,11,12]])
print(m)
print("---------------")

print(m.shape)
print("---------------")

# Arange returns evenly spaced values within a given interval
n = np.arange(0,30,2)
print(n)
print("---------------")


# Reshape returns an array with the same data with a new shape
n = n.reshape(3, 5)
print(n)
print("---------------")

# Returns evenly spaced numbers over a specified interval
o = np.linspace(0,4,9)
print(o)
print("---------------")

# Changes the shape and size of array in-place
o.resize(3,3)
print(o)
print("---------------")

# Returns a new array of given shape and type, filled with ones
print(np.ones((3,2)))
print("---------------")

# Returns a new array of  given shape and type, filled with zeros
print(np.zeros((3,2)))
print("---------------")

# Returns a 2-D array with ones on the diagonal and zeros elsewhere
print(np.eye(3))
print("---------------")

# Extracts a diagonal or constructs a diagonal array
y = [4, 5, 6]
print(np.diag(y))
print("---------------")

# Array using repeating list
print(np.array([1,2,3] * 3))
print("---------------")

# Repeat elements of an array using repeat
print(np.repeat([1,2,3], 3))
print("---------------")

# Combining arrays
p = np.ones([2,3], int)
print(p)
print("---------------")

# vstack to stack arrays in sequence vertically (row wise)
print(np.vstack([p, 2*p]))
print("---------------")

# hstack to stack arrays in sequence horizontally (column wise)
print(np.hstack([p, 2*p]))
print("---------------")

# OPERATIONS
x = np.array([1,2,3])
y = np.array([4,5,6])

print(x+y)
print("---------------")

print(x-y)
print("---------------")

print(x*y)
print("---------------")

print(x/y)
print("---------------")

print(x**2)
print("---------------")

# Dot product
print(x.dot(y))
print("---------------")

# T for transpose
print(x.T)
print(x.T.shape)
print("---------------")

# Math functions
a = np.array([-4, -2, 1, 3, 5])
print(a.sum())
print(a.max())
print(a.min())
print(a.mean())
print(a.std())
# argmax and argmin return the index of the maximum and minimum values in the array
print(a.argmax())
print(a.argmin())
print("---------------")

# Indexing / Slicing
s = np.arange(13)**2
print(s)
print("---------------")

# get the value at a specific index.
print(s[4])
print("---------------")

# : indicate a range. array[start:stop]
print(s[1:5])
print("---------------")

# double :: can be used to indicate step-size array [start:stop:stepsize]
print(s[-5::-2])
print("---------------")

r = np.arange(36)
r.resize((6,6))
print(r)
print("---------------")

# Get exact position of value in matrix
print(r[2,2])
print("---------------")

# : to select a range of rows or columns
print(r[3, 3:6])
print("---------------")

print(r[:2, :-1])
print("---------------")

# Create 4 x 3 array of random numbers 0-9
test = np.random.randint(0, 10, (4, 3))
print(test)
print("---------------")

for row in test:
	print(row)
print("---------------")

for i in range(len(test)):
	print(test[i])
print("---------------")
