import numpy as np
import sys

l = [1,5,3,4,7]
arr = np.array([1,5,3,4,7]) #

# print( l * 2) # [1, 5, 3, 4, 7, 1, 5, 3, 4, 7]
# print( arr * 2) # [2, 10, 6, 8, 14]


list_size = sys.getsizeof(l)
array_size = sys.getsizeof(arr)

print(f'List size: {list_size}')
print(f'Array size: {array_size}')

arr_median = np.median(arr)
arr_mean = np.mean(arr)

print(f'Median: {arr_median}')
print(f'Mean: {arr_mean}')