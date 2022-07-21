# def add(y,x=0):
# 	print(f'x={x}, y={y}')

# add(3,4)
# add(6)   # x=6, y=0
# add()


# ----------------------------- keyword arguments ---------------------------- #
# def greet(age, country, name="Anonymous"):
# 	print(f'Hello {name}. You are {age} years old and you are from {country}')

# greet( age=34, country='Bulgaria', name="Maria")


# greet( country='Bulgaria', age=34, name="Maria")


# def concat(obj, axis=0, join='outer'):
# 	print(f'obj = {obj}')
# 	print(f'axis = {axis}')
# 	print(f'join = {join}')

# concat([1,2,3])

# ----------------------------------- *args ---------------------------------- #

# def add1(args):
#   print( sum(args) )

# add1((3,))
# add1((3,4))
# add1((3,4,5))


# def add2(*args):
#   	print(args)

# add2(3)
# add2(3,4)
# add2(3,4,5)


# --------------------------------- **kwargs --------------------------------- #
# def foo( **kwargs):
# 	print(kwargs)

# foo(x=1)
# foo(x=1,y=2)
# foo(x=1,y=2,z=3)

# ---------------------------------- example --------------------------------- #
# def magic_foo(x,y, *args, **kw):
# 	print(args) # ()
# 	print(kw)   # {z:7}


# # magic_foo(1,2)
# magic_foo(1,2,z=7)

# --------------------------------- example 2 -------------------------------- #
# def greet(name, age, country):
# 	print(name, age, country)

# user_data = ['Ada', 23, 'Bulgaria']

# greet(user_data[0],user_data[1], user_data[2])
# greet( *user_data )

# --------------------------------- example 3 -------------------------------- #
# def foo(*x):
# 	# x = (3,4,5)
# 	pass

# foo( 3,4,5 )

# data = (1,2)
# x,y = data
# print(x, y)



# --------------------------- function return value -------------------------- #
# Math:
# Фунцкция :взаимно еднозначно съответствие: X => Y

# y = f(X)
# f(X) => y

# 1,2 => 3
# 2,4 => 6

# def cub_sum(*args):
# 	# args  = (1,2,3,4)
# 	sum = 0
# 	for arg in args:
# 		# sum = sum + arg**3
# 		sum += arg**3

# 	return sum


# cub_sum(1,2) => 1**3 + 2**3 = 9
# cub_sum(1,2,3) => 1**3 + 2**3 + 3**3 = 9 + 27 = 36

# res = cub_sum(1,2) + cub_sum(1,2,3)
# print(res)


def foo(x,y):
	return x+y
	print(x,y)

print( foo(2,3) )
print( 2+2 )