# Searching Array : -> you can search an  array for a certain value and return the indexes that get the match.

import numpy as np
ar1=np.array([1,2,3,4,5,4,4,4,])
arr_new=np.where(ar1 == 4)
print(arr_new)      # OUTPUT: -> (array([3, 5, 6, 7], dtype=int64),)  it will print the index where 4 is present


# find the ..index...where the values are EVEN:
import numpy as np 
ab1=np.array([1,2,3,4,5,6,7,8,])
even_num=np.where(ab1%2==0)
print(even_num)     # OUTPUT: -> (array([1, 3, 5, 7], dtype=int64),)


# Now we will find the ..index...where the values are ODD:
import numpy as np
ab1=np.array([1,2,3,4,5,6,7,8])
odd_new=np.where(ab1%2==1)
print(odd_new)

# OUTPUT:-> (array([0, 2, 4, 6], dtype=int64),)    It will print the index




# searchsorted()- perform binary search in array.
# we wil the find the index where the value 7 is present.
import numpy as np
b1=np.array([6,7,8,9])
b21= np.searchsorted(b1 ,7)
print(b21)      # OUTPUT:-> 1   -> index 


b22=np.where(b1==7)
print(b22)        # OUTPUT:-> (array([1], dtype=int64),)


# now we will search from right side
import numpy as np
b1=np.array([6,7,8,9])
b21=np.searchsorted(b1 , 7, side='right')
print(b21)          # OUTPUT:-> 2   -> index 