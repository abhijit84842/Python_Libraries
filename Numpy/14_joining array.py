# Joning the numpy array -> here for this we will pass the concatenate()

# joining of 1-D
import numpy as np
x=np.array([1,2,3])
x1=np.array([4,5,6])
new_arr=np.concatenate((x ,x1))
print(new_arr)
# OUTPUTL:-> [1 2 3 4 5 6]


# Joning of 2-D arrays along with rows(axis=1)
import numpy as np
a1=np.array([[1,2], [3,4]])
a2=np.array([[5,6], [7,8]])
add_ele1=np.stack((a1,a2) , axis=1)
add_ele2=np.concatenate((a1,a2) , axis=1)
print(add_ele1)

'''
OUTPUT:
[[[1 2]
  [5 6]]

 [[3 4]
  [7 8]]]
'''

'''
OUTPUT:
[[1 2 5 6]
 [3 4 7 8]]
'''

# Joining the array using the stack function:
import numpy as np
x=np.array([1,2,3])
x1=np.array([4,5,6])
add1= np.stack((x , x1) , axis=1)
print(add1)

'''
OUTPUT:
[[1 4]
 [2 5]
 [3 6]]
'''


# Stack along with rows : hstack()
import numpy as np
x=np.array([1,2,3])
x1=np.array([4,5,6])
add1=np.hstack((x,x1))
print(add1)     # OUTPUT: -> [1 2 3 4 5 6]


