# Shape of an array :- the shape of an array is the number of elements in each dimensions.


# now we will try to get the shape of an array
import numpy as np 
a=np.array([[1,2,3,4] , [5,6,7,8]])
print(a.shape)      #   OUTPUT:-> (2, 4)
# OUTPUT Explain:-> 2 is number of dimension and 4 is number of element present in each dimensions.



# Now we will create 5-D array using ndmin:
x2=np.array([1,2,3,4] , ndmin=5)
print(x2)   # Output -> [[[[[1 2 3 4]]]]]

print(f"The shape of array is {x2.shape}")                 # Output ->  The shape of array is (1, 1, 1, 1, 4)
