# x = 'a'
# y = int(x)

# t = (3,4,5)
# l = list( t )
# print(l)

# str1 = 'abc'
# l = list(str1)
# print(l) # 'abc' ['a', 'b', 'c']


# for el in (5,):
# 	print(el)


# ------------------------------- del operation ------------------------------ #
# l = [1,2,3]
# del l[1]
# print(l)

# ---------------------------- other list methods ---------------------------- #
# list.extend(iterable)
# l1 = [1,2,3]
# l1.extend('abc')
# print(len(l1))

# list.append(x)
# l1 = [1,2,3]
# l1.append('abc')
# print(l1)

# list.remove(x)
# l1 = [1,2,3,1]
# l1.remove(1)
# print(l1)

# # list.pop([i])
# l1 = [1,2,3]
# x = l1.pop(1)
# print(l1)
# print(x)

# list.count(x)
# l1 = 'alabala'
# count_a = l1.count('a')
# print(count_a)

# ------------------------------- List of Lists ------------------------------ #
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# # print( matrix[-1][-2] )
# # print( matrix[2][1] )
# # print( matrix[1,1] )

# import numpy
# real_matrix = numpy.array(matrix)
# print(real_matrix[:,1])

# ------------------------------ more on tuples ------------------------------ #
# fruits = ["apple", "banana", "strawberry", "banana", "orange"]
# fruits = tuple(fruits)


# fruits[0] = 4
# print(fruits)

# r = range(1,20,2)
# print(tuple(r))

# x = 5
# user_name = 'ada'

# print( user_name + str(x))

users = (
    ["Ivan", "Ivanov", 34],
    ["Maria", "Ivanova", 36],
    ["Asen", "Asenov", 20],
)

for user in users:
	print(user[2])


# 34
# 36
# 20









