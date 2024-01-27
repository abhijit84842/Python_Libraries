# sort()- the numpy ndarray object has a function which is called sort(), and thi will sort a specified array.

import numpy as np 
a1=np.array([0,5,1,3,7,2])
print(np.sort(a1))
# OUTPUT : -> [0 1 2 3 4]


# sort the array alphabetically
import numpy as np
x1=np.array(['banana','apple','cherry'])
print(np.sort(x1))
# OUTPUT : -> ['apple' 'banana' 'cherry']



# sort the boolean array:
import numpy as np
x2=np.array([True,False,False,True])
print(np.sort(x2))  # OUTPUT : -> [False False  True  True]


# sorting the 2-D array
import numpy as np 
x3=np.array([[3,4,2], [5,0,1]])
print(np.sort(x3))

'''
OUTPUT : ->
[[2 3 4]
 [0 1 5]]


'''
