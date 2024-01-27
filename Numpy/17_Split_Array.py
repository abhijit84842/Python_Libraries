# Spliting Array: -> it break the array
#split()
# array_split()


#split()
# split 1-D array in 3 part
import numpy as np 
arr1=np.array([1,2,3,4,5,6])
splited_arr=np.split(arr1 , 3)
print(splited_arr)      #OutPut; -> [array([1, 2]), array([3, 4]), array([5, 6])]




# split 1-D array in 4 part
# array_split()
import numpy as np
arr1=np.array([1,2,3,4,5,6])
arr_new=np.array_split(arr1, 4)
print(arr_new)

# OUTPUT: -> [array([1, 2]), array([3, 4]), array([5]), array([6])]



# split into array with index
import numpy as np
arr1=np.array([1,2,3,4,5,6])
arr_new=np.array_split(arr1, 3)
print(arr_new[0])
print(arr_new[1])
print(arr_new[2])

'''
OUTPUT:
[1 2]
[3 4]
[5 6]
'''


# splinting the 2-D array
import numpy as np
a1=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
new_b20= np.array_split(a1, 3 , axis=1)
print(new_b20)