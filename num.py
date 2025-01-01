
import numpy
ar=numpy.array([1,2,3,4,5,6,7,8,9,10])
print(ar)
print(ar[1])
print(ar[2]+ar[3])
print(ar[1:5])
print(ar[4:])
print(ar[:4])
print(ar[-3:-1])
print(ar[1:10:2]) 



import numpy as np
ar=np.array([1,2,3,4,5])
print(ar)
a=[]
print(type(a))
print(type(ar))


import numpy as np
print(np.__version__)
ar=np.array([[1,2,3],[4,5,6,]])
print(ar)
print('2nd element on 1st row:',ar[0,1] )

import numpy as np
ar=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(ar[0,2])
print("1.",ar[1,1:4])
print("2.",ar[0:2,2])
print("3.",ar[0:2,1:4])

import numpy as np
ar=np.array([[1,2,3,4,5],[6,7,8,9,10]]) 
print(ar[0:2])
print(ar[1:])
