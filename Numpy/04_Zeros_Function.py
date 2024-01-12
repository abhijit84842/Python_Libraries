# zeros() use to create array with zero filled..
# its default datatype is float

import numpy as np 

a=np.zeros(5)       # we have to mention the shape of array
print(a)        # [0. 0. 0. 0. 0.]

# but we can change the datatype
a=np.zeros(5 , dtype=int)
print(a)        # output-> [0 0 0 0 0]