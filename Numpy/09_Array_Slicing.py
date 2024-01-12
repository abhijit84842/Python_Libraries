# Slicing Array= in python sclicing means taking elements from one given index to another index.
# exapmle => [start : end], [start:end:step]

# now we will slice an element from 2 to 5.
import numpy as np 
x=np.array([1,2,3,4,5,6,7,8,9])
print(x[1 : 5])    # OUTPUT -> [2 3 4 5]
print(x[1 : 7])        # OUTPUT ->   [2 3 4 5 6 7]



# now we will slice from index 4 to the end value
import numpy as np
x1=np.array([1,2,3,4,5,6,7,8,9])
print(x1[4 : ])         # OUTPUT ->   [5 6 7 8 9]


# now we will slice the element from begining to index 4
x2=np.array([1,2,3,4,5,6,7,8,9])    
print(x2[ :4])      # OUTPUT -> [1 2 3 4]