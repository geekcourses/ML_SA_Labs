# list, tuple, string, range

# ----------------------------------- List ----------------------------------- #
# student1 = 'Maria'
# student2 = 'Pesho'
# student3 = 'Ivan'

# students = ['Maria', 'Pesho', 'Ivan']

# print(student1)
# print(students[0])

# RAM:
#     student1: 0x123: 'Maria'
#     student2: 0x145: 'Pesho'
#     student3: 0x134: 'Ivan'

#  students:
#     students[0]:0x213:'Maria',
#     students[1]:0x213:'Pesho',
#     students[2]:0x213:'Ivan'


# l = [ 1, 'a', [4,5] ]
# print( len(l) )
# print('a'*3) # 'aaa'
# l = [ 1+2, 'a'*3 ]
# print(l)  # [3, 'aaa']
# print(len(l))


# Example:
# l1 = [1,2,3]
# x = 7
# l2 = [ l1[0], l1[1], x ]

# RAM:
#     l1[0]:0x131 =>  1
#     l1[1]:0x124 =>  2
#     l1[2]:0x128 =>  3
#         x:0x228 =>  7
#     l2[0]:0x567 =>  1
#     l2[1]:0x527 =>  2
#     l2[2]:0x787 =>  7

# l1[0] = 9
# print(l1)
# print(l2)


# l = [1,2,1,1,1,1]
# s = {1,2,1,1,1,1}
# print(l)
# print(s)

# l = []
# print(len(l))
# print(type(l))

# List of Lists
# m = [
#     [1,2,3],
#     [4,5,6]
# ]

# print( m[1][1] )


# -------------------------------- Copy list -------------------------------- #

# x = 1
# y = x  # copy by value
# x = 9
# print(x,y)

# x = [1]
# y = x  # copy by reference
# x[0] = 9
# print(x,y)

# RAM:
#     x: 0x123 => 1
#     y: 0x567 => 1

#     x: 0x234 =>0x432,
#  x[0]: 0x432 => 9
#     y: 0x321 =>0x234


# ----------------------------------- tuple ---------------------------------- #
# l = [1]
# t1 = (1)
# t2 = (1,)
# print( t1)
# print( t2)

# t1 = (1,2,3)
# t2 = 1,2,3

# print(t1)
# print(t2)


# birth_date = (12, 1, 1990)

# l = [1,2,3]
# t = (1,2,3)

# l[0] = 9
# t[0] = 9

# t = (
#      [1,2],
#      [3,4]
# )

# t[0] = [] # error

# l = t[0]
# l[0] = 9
# print(t)


# ----------------------------------- range ---------------------------------- #
# for _ in range(3):
# #     print('hi')

# import sys

# l1 = [1,2,3]
# l2 = [1,2,3,4,5,6,6,6,6,6,6,1,2,3,4,5,6,6,6,6,6,6]

# print( sys.getsizeof(l1) )
# print( sys.getsizeof(l2) )

# r1= range(1,4)
# r2= range(1,1_000_000)

# print( sys.getsizeof(r1) )
# print( sys.getsizeof(r2) )

# l = [1,2,3]
# r = range(1,9)

# print( l )
# print( list(r) )



# range(start, stop, step)
# r = range(5)   # 0, 1, 2, 3, 4
# print( list(r) )


# r = range(10, 0, -2)
# print( list(r) )     # 10, 8, 6, 4, 2,


# r = range( 1, -10, 1)
# print( list(r) )



# ---------------------------- Sequence Operations --------------------------- #
# l1 = [1,2,3]
# l2 = [4,5,6]

# print( 'a' + 'b') # 'ab'
# print(l1 + l2)
# print(l1 * 3)

# import numpy as np

# arr1 = np.array(l1)
# arr2 = np.array(l2)

# # print(arr1 + arr2)
# print(arr1 * 3)



# l = [1,2,3]
# print( 6 not in l )
# if 6 in l:
#     print('Yes')
# else:
#     print('No')


# Indexing
# l = list( range(1,10) )
# print(l)
# print(l[-1])
# print( l[len(l)-1] )
# print(l[-2])

# print( len(l) )

# string1 ='abc'
# print( string1[-1] )


# Slicing
# sliced = sequence[start:end:step]
# l = [1,2,3,4,5]
# l2 = l[2::]
# print(l2)

# print( l[:3] )

# print( l[::2] )  #indexes => 0,2,4

# name = 'abcdef'
# # print( name[-1:-4:-1])
# print( name[::-1] )



# user_name = "iv"

# for i,el in enumerate(user_name):
#     print( el + str(i))



# x, y  = [1,2]
# print(x)
# print(y)


# point3d = (4, 0, 3)
# point3d_list = list(point3d)
# point3d_list[0] = 9
# print( point3d_list )
# point3d = tuple(point3d_list)
# print( point3d )


# string = 'abc'
# l = list(string)
# print(l)

# l = [1,2,3]
# print( str(l) )


# # List methods
# l = [1,2,3]
# l.append(9)
# print(l)

l = [2,5,3,8]
max_el = max(l)
print(l.index(max_el))
