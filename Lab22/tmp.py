import numpy as np

raw_data = [1,2,3,4,5]
data1 = np.array(raw_data)

# print(f'sum: {sum(raw_data)}')
# print(f'count: {len(raw_data)}')
# print(f'mean: {sum(raw_data)/len(raw_data)}')

mean = data1.mean()
# print(f'mean: {mean}')

sum_of_square_differences = np.sum( (data1-mean)**2 )
# print(sum_of_square_differences)

N = data1.size
variance = sum_of_square_differences/N
print( variance )
print(f'np.var:{np.var(data1)}')

std = np.sqrt(variance)
print(f'std: {std}')
print(f'np.std: {np.std(data1)}')





