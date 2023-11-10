# numpy seminar

# create a numpy ndarray object
# import numpy as p
# arr = p.array([1, 2, 3, 4, 5])
# print(arr)
# print(type(arr))


# check no:of dimensions
# import numpy as np

# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# access 2d array
# import numpy as np
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('2nd element on 1st row: ', arr[0, 1])
# print('5th element on 2nd row: ', arr[1, 4])

# access 3d array
# import numpy as np

# arr = np.array([[[1,2,3],[1,2,3],[1,2,3]],
#                 [[2,2,3],[2,2,3],[2,2,3]]])
# print(arr.ndim)    

# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[1:5:2])

# print(arr[1:2])


# slicing in 1d/negative slicing/slicing in 2d
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:5])

import numpy as np
a=np.array([[[1,2,3],[1,3,4]]])
print(a.ndim)