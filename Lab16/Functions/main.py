# def function_name(param_list):
#   '''docstring'''
#   statements
#   return [expression]


# def add(x,y):
#     """ Print sum of two numbers

#         Args:
#             x (int): 1st number to add
#             y (int): 2d number to add
#     """
#     # x = 2,y=3
#     print(x+y)

# x = 1

# # RAM:
# #     x:0x123=>1
# #   add:0x342=>[function add]

# add(2,3)


# ---------------------------- Default parameters ---------------------------- #
# def foo(x=1,y=2):
#     print(f'x={x}', end=';')
#     print(f'y={y}')

# foo(5,6) #x=5, y=6
# foo(9)   #x=9, y=2
# foo(2)   #x=2, y=2
# foo()    #x=1, y=2


# ---------------------------- Keyword Argwuments ---------------------------- #
# def preaty_print_msg( msg, symbol='*', number=30 ):
#     """preaty_print_msg"""
#     print(symbol*number)
#     print(msg)
#     print(symbol*number)


# preaty_print_msg('Howdy', '~' ,number= 50)


# ----------------------------------- *args ---------------------------------- #
# def add(*arg):
#     # arg=(1,2)
#    print(arg)


# add( 1,2)
# add( 1,2,3 )
# add( 1,2,3,10 )

### example
# def foo(*args, x):
#     #args=(1,2,2,2)
#     #x=1
#     print(args)
#     print(x)

# foo(x=1)

# foo(1,2,2,2, x=9)
# # foo(1,2)
# # foo(1,2,3)


### example
# def foo(x, *args):
#     print(f'x={x}')
#     print(f'args={args}')


# foo(1)
# foo(1,2,3)


# def foo( *objects, sep=' ', end='\n' ):
#     print(f'objects={objects}')
#     print(f'sep={sep}')
#     print(f'end={end}')
#     print('END')


# foo( 1,2,3,'-', end='***', sep='---' )



# print(1,2,3, sep='-', end=';')
# print('END')


# --------------------------------- **kwargs --------------------------------- #
# def foo(**kw):
#     # kw = {'x':1,'y':3}
#     print(kw)


# foo()
# foo(x=1)
# foo(x=1, y=3)


# def foo(x, **kw):
#     print(x, kw)


# foo(y=1, z=1)


### example
# def foo(x, *args, **kwargs):
#     print(f'x={x}')
#     print(f'args={args}')
#     print(f'kwargs={kwargs}')



# foo(1,2,3, name='Ada', age=23)


### example:
# def signup(name, password, **kwargs):
#     print(name)
#     print(password)
#     print(kwargs)

#     if kwargs.get('mail',None):
#         print(kwargs['mail'])


# signup('Ada', '1234', mail='ada@gmail.com')



# --------------------------- unpack arguments (*) --------------------------- #
# def signup(name, password):
#     print(name)
#     print(password)


# # user_data = ('Ada', '1234')

# # # signup( user_data[0], user_data[1])
# # signup( *user_data )

# user_data = {
#     'password':'1234',
#     'name':'Ada'
# }

# # signup( user_data['name'], user_data['password'] )
# signup( **user_data )

# ---------------------------------- return ---------------------------------- #
# def add(x,y):
#     print(f'x+y={x+y}')
#     return x+y



# print( add(2,3) )
# # print( 5 )


