# reshaping -> means changing the shap of an array, like adding and removing the elements.

# reshaping from 1-D to 2-D
import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
b=a.reshape(4,3)              # -> devided in 4 array and every array contain 3 elements.

print(b)        # OUTPUT : -> [[ 1  2  3]   [ 4  5  6]  [ 7  8  9]  [10 11 12]]



# reshaping from 1-D to 3-D
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x1=x.reshape(2,3,2)
print(x1)         # OUTPUT : -> [[[ 1  2][ 3  4][ 5  6]] , [[ 7  8][ 9 10][11 12]]]




# unknown dimension- you are only allowed to have one unknown demension. pass -1.
y=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y1=y.reshape(2,2, -1)
print(y1)



# Flattening the array by coverting multidimensional array in 1-D.
import numpy as np
a1=np.array([[1,2,3] , [4,5,6]])
a11=a1.reshape(-1)
print(a11)          # OUTPUT : -> [1 2 3 4 5 6]

