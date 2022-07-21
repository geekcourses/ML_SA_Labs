# x = 1

# def foo():
# 	x = 2

# 	print(f'y in foo: {y}')

# def bar(x,y):
# 	print(f'x,y in bar: {(x,y)}')
# 	x+=1


# foo()
# bar(3,4)

# print(f'x in main: {x}')
# print(f'y in main: {y}')

# # local_bar = {
# # 	x: 4,
# # 	y: 4
# # }

# # global = {
# #   y: 3
# # 	x: 1,
# # 	foo: function,
# # 	bar:function..
# # }



# def add(x,y):
# 	return x+y

# x = 1
# y = 2

# print( add(x,y) )



# ----------------------- example function in funciton ----------------------- #
# def foo():
# 	print(f'x in foo: {x}')

# 	def bar():
# 		print(f'x in bar: {x}')

# 	bar()

# x = 1
# foo()
# print(f'x in main: {x}')

# x in foo:
# x in bar: 2

# local_bar = {

# }

# local_foo = {
# 	bar: function...
# }

# global = {
# 	foo:...
#     x: 1
# }


# -------------- sum is defined in built-in functions Namespace -------------- #
def foo():
	print(sum)

foo()