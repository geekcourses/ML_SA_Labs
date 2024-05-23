import numpy as np

data1 = np.array([1,2,3,4,5])
data1_mean = np.mean(data1)

sqrt_differences = (data1-data1_mean)**2
print(sqrt_differences)

var = np.sum(sqrt_differences) / data1.size
print(f'our variance: {var}')
print(f'np variance: {np.var(data1,)}')

std = np.sqrt( var )
print(f'our std: {std}')
print(f'np std: {np.std(data1)}')



