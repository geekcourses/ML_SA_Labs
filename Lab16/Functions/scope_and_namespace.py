
# ---------------------------- Scope and namespace --------------------------- #
def foo():
    x = 999
    # print(f'x in foo: {x}')

x = 1
foo()
# print(f'x in global: {x}')


# print( globals() )

# print(__file__)


# # stores the mapping from names to objects
# global = {
#     'foo':0x125 ([function foo])
#     'x': 0x123 (1)
# }


# foo = {
#     'x':0x543 (999)
# }
