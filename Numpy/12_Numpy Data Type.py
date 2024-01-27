# data types in python : string, intiger,float,boolean, complex.

# data type in numpy
# i for integer
# b for boolean
# u for unsigned integer
# f for float
# c for complex
# m for timedelta
# M for datetime
# O for object
# S for string
# U for unicode string
# V for memory

# checking the data type of numpy array -dtype
import numpy as np
x=np.array([1,2,3,4])
print(x.dtype)

# checking the data type of numpy array -string
import numpy as np
x=np.array(["a","b","c"])
print(x.dtype)

# creating array with a defined data type :
import numpy as np
x=np.array([1,2,3,4] , dtype='S')
print(x)
print(x.dtype)

# Now we will create an array with data type of 4 byte int:
import numpy as np
x=np.array([1,2,3,4] , dtype='i4')
print(x)
print(x.dtype)
