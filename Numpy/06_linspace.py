# use to create array filled evenly spaced values..
#linspace(strat,stop, num=)

import numpy as np 
a=np.linspace(1,50 ,num=4)
print(a)        # Output-> [ 1.         17.33333333 33.66666667 50.        ]



a=np.linspace(1,100, num=5, endpoint=False)     # if i don't want to include 100
print(a)

# output -> [ 1.  20.8 40.6 60.4 80.2]

a=np.linspace(1,100, num=5, retstep=True)       # find the difference between each number, we use retstep parameter
print(a)  
# output=>  (array([  1.  ,  25.75,  50.5 ,  75.25, 100.  ]), 24.75) 
   