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


# Negative sclicing -> index 3(positive index) to end 
x3=np.array([1,2,3,4,5,6,7,8,9])
print(x3[-6:-1])


# Step: -you will use step value to determine the step of slicing
# return every other value from index 1  to 5
x4=np.array([1,2,3,4,5,6,7])
print(x4[2 : 5 : 2])      # OUTPUT ->   [3 5] 



# now return every other number from the entire array. or print the odd number..
x5=np.array([1,2,3,4,5,6,7,8,9])
print(x5[ :  : 2])           # OUTPUT ->  [1 3 5 7 9]




# Sclicing in 2-D array : print 7,8,9
import numpy as np
x6=np.array([[1,2,3,4,5] , [6,7,8,9,10]])
print(x6[1 , 1:4])         # OUTPUT ->   [7 8 9]


# Another example of 2-D array
import numpy as np
x7=np.array([[1,2,3,4,5] , [6,7,8,9,10]])
print(x7[0:2 ,2])

       