import numpy as np

# ------------------------------ list vs arrays ------------------------------ #

arr1d = np.array( [1, 2, 3] )
print(arr1d)

l = ['Ada', 23, {"age":24}]
test = np.array(l)
print(test.dtype)