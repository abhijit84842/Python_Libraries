# difference between numpy array copy and view.

# copy=> its does not change the orginal array...
import numpy as np 
arr=np.array([1,2,3,4,5])
copy_ele= arr.copy()
copy_ele[1]=15
print(copy_ele)         # Output => [ 1 15  3  4  5]
print(arr)                  # Output =>[1 2 3 4 5]

#view => its change the orginal array....
import numpy as np 

arr1=np.array([4,5,6,7])
view_arry= arr1.view()
view_arry[2]=58

print(view_arry)    # Output => [ 4  5 58  7]
print(arr1)             # Output => [ 4  5 58  7]


