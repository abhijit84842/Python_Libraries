# Iterating Array : -> means the elements one by one or step by step. like for loop.

# Iterate the element of 1-D
import numpy as np 
a= np.array([1,2,3,4,52,63,5])
for i in a:
    print(i)


# Iterate the element of 2-D
    
import numpy as np 
arr1= np.array([[1,2,3],[4,5,6]])
for i in arr1:
    print(i)

'''
OUTPUT:
[1 2 3]
[4 5 6]

'''

# Iterate on each scaler element of the  2-D 
import numpy as np
x=np.array([[1,2,3], [4,5,6]])
for i in x:
    for j in i:
        print(j)

# Iteration in 3-D
import numpy as np 
a1= np.array([[[1,2,3],[4,5,6]] , [[7,8,9],[10,11,12]]])    
for i in a1:
    for j in i:
        for k in j:
            print(k)


# Iterating arrays using the nditer() function.
# now we will iterate on each scalar element.
import numpy as np 
y1 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
for i in np.nditer(y1):
    print(i)




# Now we will Iterate with different step sizes.
import numpy as np 
a2= np.array([[1,2,3,4] ,[5,6,7,8]])
for i in np.nditer(a2[: , ::2]):        # skip one by one value like even odd
    print(i)

'''
OUTPUT:
1
3
5
7

'''