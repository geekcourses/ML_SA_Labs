# ----------------------------------- Lists ---------------------------------- #
# TASK: store names of users
# user1_name  = 'Ada'
# user2_name  = 'Maria'
# user3_name  = 'Pesho'

# user_names = [
# 	'Ada',
# 	'Maria',
# 	'Pesho'
# ]

# GLOBAL:
# 	user1_name: 0x123321
# 	user_names: 0X3454354
# 	user_names[0]: 0X845869

# RAM:
# 	0x123321: 'Ada'
# 	0X845869: 'Ada'

# change 'Maria' to 'Marian'
# user_names[1] = 'Marian'
# print( user_names )



# ----------------------------- list are mutable ----------------------------- #
# a = 3
# b = a
# a = 9
# print(b) # 3

# GLOBAL:
# 	a: 0x7843784
# 	b: 0x3433434

# RAM:
# 	0x3433434: 3, i
#   0x7843784: 9

# a = [3]
# b = a
# a[0] = 9
# print(b) # [9], 3

# 9, [9], 3, [3]

# GLOBAL:
# 	a: 0x7857854
#a[0]: 0x3433434
# 	b: 0x7857854

# RAM:
# 	0x3433434: 9

# ---------------------- add item at the end of the list --------------------- #
user_names = [
	'Ada',
	'Maria',
	'Pesho'
]

user_name = 'Asen'
user_names.append(user_name)
# print(user_names)



# ----------------------------------- Tuple ---------------------------------- #
# user_data = ( 'Ada', 34, 'UK' )
# user_data[0] = 'Pesho'


# ------------------ change tuple element, which is mutable ----------------- #
# t = (23,[1],'Ada')
# print(t[1][0])

# t[1][0] = 9
# print(t)



# ------------------------------- range object ------------------------------- #
# l = [1,2,3,4,5,6,7,8,9]
# print(l)

# r = range(1,10,-2)

# 1,1+2,3+2, 5+2, 7+2
# print(list(r)) # 1, 4, 7

# 10, 8, 6, 4, 2
# r = range(10, 0, -2)
# print(list(r))


# ------------------------------ range use case ------------------------------ #
# # print 10 times 'hi'
# for el in range(5):
# 	print('hi')

# for el in "abc":
# 	print(el)


# ------------------------- common sequence operatons ------------------------ #
# Concatenation
# l1 = [1,2,3]
# l2 = [4,5,6]

# l = l1+l2
# print(l)

# print( [1,2,3] * 3)

# ---------------------------- membership testing ---------------------------- #
# l1 = [1,2,3]
# print( 2 in l1 )

# print( 3 in range(-2, 9, 1) )

# ---------------------------------- indxing --------------------------------- #

# l = [1,2,3,4,5]

# print(l[4])
# print(l[-1])

# string = 'abcd'
# print(string[-1])

# ---------------------------- length of sequnece ---------------------------- #
# l = "abcde"
# print( len(l) )

