# Filter Array :-> getting some elements out of existing array and creating a new array is called filtering.

# A boolean index list is a list of boolean corosponding to indexes in the array.(True and False)

# create an array from the element on index 0 to 2:
import numpy as np 
x=np.array([1,2,3])
y=np.array([True , False , True])
filter_value=x[y]           #  by default it will take the true
print(filter_value) #Output => [1 3]



# Now we will create a filter array
# that will return only values higher than 42

import numpy as np
arr1= np.array([41,42,43,25,30,90,20])
filter_array =[]
for i in arr1:
    if i > 41 :
        filter_array.append(i)
print(filter_array)


