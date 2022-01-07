"""
Week 1 Live Session
"""

# *args and **kwargs review

# a single * is the unpacking operator for iterables
# a double ** is the unpacking operator for dictionaries

# suppose we want to create a function to sum to variables
def sum_it(a, b):
    return a + b

# now suppose we want to be able to extend this function to be able
# to sum n digits.
def sum_it(int_list):
    total = 0
    for i in int_list:
        total += i
    return total

some_ints = [1, 2, 3, 4]
print(sum_it(some_ints))

# This works nicely, but we need to put the elements to sum in a list
# before we call the function on them.

def sum_it(*args):
    total = 0
    for i in args:
        total += i
    return total

# now we're not passing a list.  We're passing positional arguments.
# our function takes these arguments and packs them into an iterable object (tuple)
# called args. args is not a keyword we could just as well say *numbers.
# The unpacking operator * is the important part.
print(sum_it(1, 2, 3, 4, 5, 6, 18))

# **kwargs is similar to *args, but it accepts keyword arguments instead
# of positional arguments.
def multiple_ops(**kwargs):
    initial_sum = kwargs['add_1'] + kwargs['add_2']
    try:
        if kwargs['operation'] == 'div':
            return initial_sum / kwargs['mult_div']
    except KeyError:
        return initial_sum * kwargs['mult_div']

# here we pass a dictionary to our function (although, note that
# it isn't defined with curly braces).  Think of the keywords as keys and the values
# as values.
multiple_ops(add_1 = 7, add_2 = 8, mult_div = 2)

multiple_ops(add_1 = 7, add_2 = 8, mult_div = 2, operation = 'div')

# Again, the name kwargs is just a convention.
# We're really concerned with the ** unpacking operator.

# An example using *args and **kwargs
# This function takes *args and *kwargs as parameters.
# The function loops through all arg values and multiplies them to get iterations.
# We then loop over the range of iterations and if the iterator is even
# we print kwargs values else we print kwargs keys.

def do_something(*args, **kwargs):
    iterations = 1
    for arg in args:
        iterations *= arg

    for i in range(iterations):
        if i % 2 == 0:
            print(kwargs.values())
        else:
            print(kwargs.keys())

do_something(1, 2, 3, 4, 5, foo = 'hello', bar = 'hi')

# what happens if I try to specify the key word arguments before the positional arguments?
do_something(bar = 'hi', foo = 'hello', 1, 2, 3)

# another function using *kwargs
def p_func(**kwargs):
    for i in kwargs.values():
        print(i)

# Notice the error generated when we call the function on the following input.
p_func('a', 'b', 'c', 'd')

p_func(arg1 = 'a', arg2 = 'b', arg3 = 'c', arg4 = 'b')

# Writing functions with standard arguments, *args and *kwargs
# Note that the order is critical here.
# Standard arguments precede *args, which precede **kwargs.

# Note that the single unpacking operator (*) can be used on any iterable.
# The ** unpacking operator can only be used on dicts.

# to get a better sense of what the unpacking operator does
# notice how calling print on the list prints the brackets, commas and quotes (the list itself)
print(['foo', 'bar'])
# calling print on the unpacked list prints just the list content
print(*['foo', 'bar'])

# this is the same as calling print with two arguments...
print('foo', 'bar')

# passing unpacked args to a function with a specified number of arguments
def print_something(a, b):
    print(a, b)

# this allows us to pass in the two required parameters with unpacking
print_something(*['foo', 'bar'])

# here we're unpacking too many values
print_something(*['foo', 'bar', 'norf'])

# another printing function using *args
def print_something(*args):
    hold = ''
    for i in args:
        hold += str(i) + ' '
    print(hold)

# consider passing multiple lists to the above function.
# the unpacking operator in *args will treat these as a tuple of lists.

# we can use unpacking operators on our function inputs as well as within the function.
# Here we use multiple unpacking operators to unpack three lists and pass those values
# as *args...they will then be packed into a tuple and further unpacked within the function.
print_something(*[1, 2, 3], *[4, 5, 6], *[7, 8, 9])

# without the additional level of unpacking we're just concatenating the lists
print_something([1, 2, 3], [4, 5, 6], [7, 8, 9])

"""Now a bit of numpy review.

Matplotlib uses the numpy ndarray data structure, so it's important to have a good grasp on these.
"""

import numpy as np

# numpy's array method takes any list, tuple or array-like object and converts it to an ndarray

an_array = np.array([i for i in range(10)])
print(an_array)
print(type(an_array))

# nested arrays are arrays that have arrays as values

# a 0-D array is just a scalar...each value in a 1D array is a 0-D array itself
scalar = np.array(20)

# a 1-D array has scalars as its elements.  Think of a single vector of scalars.
basic_array = np.array([1, 2, 3, 4, 5])
print(basic_array)

# a 2-D array is just an array of arrays. Think of a matrix or table.
two_dim_array = np.array([[1, 2, 3], [4, 5, 6]])
print(two_dim_array)
# we can evaluate the shape attribute of ndarrays as well
print(two_dim_array.shape)

# a 3-D array has 2-D array elements.
three_dim_array = np.array([[[2, 4, 6], [8, 10, 12]], [[14, 16, 18], [20, 22, 24]]])
print(three_dim_array)

# the ndim attribute gives the number of dimensions in an ndarray
print(three_dim_array.ndim)

# Note that ndarrays can have any number of dimensions.
# np.array() takes an optional argument ndmin to specify dimensions.

# Indexing

# we index 1D arrays just like lists and tuples
one_dim = np.array([i for i in range(10)])
print(one_dim[1:5])

# to index 2D arrays we use comma separated values to address dimension and index
# think of the 1st dimension as the row and the index as the column
two_dim = np.array([[1, 2, 3], [4, 5, 6]])
print(two_dim[1, 2])
print(two_dim[0, 0])

# higher dimensional arrays are indexed similarly, the first integer represents the first dimension,
# the second integer represents the second dimension and so on.
three_dim = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(three_dim)
print(three_dim[0, 1, 2]) # prints third element of second array of first array
# above the 0 allows us to access the first 2D array...see below
print(three_dim[0])
# from there on the next two positions are just accessing values within the first 2D array
print(three_dim[0, 1]) # this returns second row from first 2D array

# Here we're accessing the second 2D array and then the first row of that array and the second row element.
print(three_dim[1, 0, 1])

# We can use negative indexing as well.
# Here we access the last element of the last row of the last 2D array.
print(three_dim[-1, -1, -1])
# and here we access the first element of the last row of the first array
print(three_dim[0, -1, 0])
# and now the first element of the first row of the first array
print(three_dim[0, -2, 0])

# Slicing is also similar to what we've experienced with lists and tuples
# we slice with [start: end] or [start: end: step]
# as before, omitting the starting index assumes zero
# and omitting the end assumes the length of the array

# We'll skip an explanation of slicing 1D arrays and jump to higher dimensions
two_dim = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# Here we're slicing from index 1 to 3 of the second dimension (dimension index 1)
print(two_dim[1, 1:3])

# Now we're accessing the last two values from both dimensions
# This will return a 2D array
print(two_dim[0:2, 2:4])

# the following does the same as the preceding line
print(two_dim[:, 2:4])

# 3D arrays are sliced similarly
three_dim = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12], [13, 14, 15, 16]]])

# accessing last two elements of last row of second 2D array.
print(three_dim[1, 1, 2:])

# returns a 2D array
print(three_dim[0:2, 1, 1:])
# returns a 3D array
print(three_dim[0:2, 0:2, 1:])

# Data Types
# Numpy supports strings (S), integers (i), floats (f), bools (b) and complex numbers (c)
# and also has some additional data types such as:
# unsigned integer (u), timedelta (m), datetime (M), object (O), unicode string (U)

# ndarrays have an attribute dtype that will reveal the datatype of the array
two_dim = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(two_dim.dtype)

foo = np.array([i for i in 'abcdefg'])
print(foo.dtype)

# notice that the dtype here was unicode string
# we can be explicit about the dtype when creating an array

foo = np.array([i for i in 'abcdefg'], dtype = 'S')
print(foo.dtype)

# size can also be specified for i, u, f, S and U
foo = np.array([15, 16, 17, 16,], dtype = 'S2')
print(foo.dtype)

# notice what happens when we specify single byte string dtype with these ints...our values are truncated.
foo = np.array([15, 16, 17, 16,], dtype = 'S1')
print(foo)

# an exception will occur if you try to specify a dtype to which the values in the array can't be cast

# oftentimes you need to cast an entire array to another type
# numpy offers the method astype() which takes the new type as a parameter and returns a copy.
# datatypes can be specified with the single char version or the name. For example 'f' or float.

an_array = np.array([1, 2, 3, 4, 5])
an_array.astype('S') # this will just return a copy, so we need to assign it to a variable or overwrite it

an_array = an_array.astype('S')
print(an_array.dtype)


fl_array = np.array([1.2, 2.5, 2.7, 2.9, 2.1])
# print a copy of the array with dtype changed from float to integer
print(fl_array.astype('i'))

# copy() and view() methods
# These concepts are related to the aliasing of variables

# In numpy we can use the copy() method to make copies of arrays.
# Changes made to the original or the copy have no impact on another.
# A view() of an array just points to the original array, so changes made
# to the original or the view will impact the other.

# .copy()
an_array = np.array([1, 2, 3, 4])
a_copy = an_array.copy()

an_array[0] = 99
a_copy[1] = 99

print(an_array)
print(a_copy)

# .view()
an_array = np.array([1, 2, 3, 4])
a_view = an_array.view()

an_array[0] = 99
a_view[1] = 99

print(an_array)
print(a_view)

# We can think about this in terms of ownership of the data.
# A copy owns the data and a view does not.
# Data ownership can be assessed using the base attribute of an ndarray.

an_array = np.array([1, 2, 3, 4])
a_copy = an_array.copy()
a_view = an_array.view()

# If the array owns the data the base attribute will return None
# If not the base attribute returns a reference to the original object
print(a_copy.base)
print(a_view.base)

# if we modify an element in the original array returned from the base attribute
# it will modify the original array.
a_view.base[0] = 99

# now if we print the original array, the copy and the view,
# the original and the view will have been modified by the preceding statement.
print(an_array)
print(a_copy)
print(a_view)

# the shape attribute returns a tuple (of length .ndim) with the corresponding number of elements in that index
one_dim = np.array([1, 2, 3, 4])
two_dim = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
three_dim = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]])

print(one_dim.shape) # one dimension with 4 elements
print(two_dim.shape) # two dimensions with 4 elements. Or two rows and 4 columns.
print(three_dim.shape) # three dimensions. Two three x four 2D arrays.

# resahpe()
# The reshape method allows us to change the shape of an array or add/remove elements from dimensions.
# You can reshape into any array as long as you have enough elements to achieve that shape.
# for example, if we had a 1D array of length 9 then we couldn't reshape into a 2D array of shape (2, 5)
an_array = np.array([i for i in range(1, 21)])

new_array = an_array.reshape(4, 5)
print(new_array)

three_dim = an_array.reshape(2, 5, 2)
print(three_dim) # now we have 3D array consisting of two five x two arrays

# Note that reshaping returns a view
print(an_array.reshape(2, 5, 2).base)

# so if we alter a value in the reshaped array then we'll alter the original array we reshaped.
an_array.reshape(2, 5, 2)[0, 0, 0] = 99
print(an_array)

# We assigned the reshaped object to the variable three_dim, and changes made here
# will also be reflected in the original array
print(three_dim.base)

# this operation will also have an impact on our original array.
three_dim[0, 0, 1] = 99
print(an_array)

# Note that we can avoid this by saving a copy of the view.
one_dim = np.array([1, 2, 3, 4, 5, 6, 7, 8])
two_dim = one_dim.reshape(4, 2).copy()
two_dim[0, 0] = 99
print(two_dim.base)
print(two_dim)
print(one_dim)


# We can also initialize the values of the array generally

# np.zeros() takes a shape and will initialize an ndarray
print(np.zeros(10))

three_dim_z = np.zeros((2,3,4))
print(three_dim_z)

# np.ones()
print(np.ones(10))

two_dim_ones = np.ones((4,4))
print(two_dim_ones)

# np.random.random()
print(np.random.random(10))

two_dim_rand = np.random.random((4, 4))
print(two_dim_rand)

# np.arange() similar to range()...takes start stop and step values

three_dim = np.arange(1, 51).reshape(5, 2, 5)
print(three_dim)

# operations between two vectors
# numpy allows us to easily do operations between arrays
print(two_dim_ones + two_dim_rand)
print(two_dim_ones / two_dim_rand)

# we can also do operations between scalars and ndarrays
# this gives us a good toolset for performing matrix operations.
print(two_dim_ones * 1.5)

# There are a number of array methods that provide valuable aggregate information
# .min(), .max(), .sum(), mean(), std()
print(two_dim_rand.max())
print(two_dim_rand.min())
print(two_dim_rand.sum())
print(two_dim_rand.mean())
print(two_dim_rand.std())

# get the mean of first column of two_dim_rand
print(two_dim_rand[:,0].mean())

# we can specify the axis of the ndarray to accomplish this as well
# axis 0 computes along rows and axis 1 computes along columns
print(two_dim_rand.mean(axis = 1)) # aggregates along column, so will return means for each row
print(two_dim_rand.mean(axis = 0)) # aggregates along rows, so will return means for each column

# We can calculate dot products with the .dot() method
array_1 = np.array([1, 2, 3, 4])
array_2 = np.array([1, -2, -3, 4])

print(array_1.dot(array_2))

# another dot product
vector = np.array([1, 2, 3]) # 1x3
matrix = np.array([[1, 2], [1, 1], [2, 1]]) # 3x2

print(vector.dot(matrix))

# transposition
matrix = np.random.random((2, 4))
print(matrix)
print(matrix.T)

# Iterating over ndarrays

# prints elements
for i in np.array([i for i in range(10)]):
    print(i)

# prints rows
for i in np.arange(1,21).reshape(4, 5):
    print(i)

# prints 2-D matrices
for i in np.random.random((2,5,2)):
    print(i)

# nditer()
for i in np.nditer(np.random.random((2,5,2))):
    print(i)

# ndenumerate
for i, j in np.ndenumerate(np.random.random((2,5,2))):
    print(i, j)