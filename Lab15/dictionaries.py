# ------------------------------- List vs Dict ------------------------------- #
# l = [1,2,3]
# d = {
#     'one':1,
#     'two':2,
#     'three':3
# }

# RAM:
    # l[0]: 0x123: 1
    # l[1]: 0x133: 2
    # l[2]: 0x127: 3
    # d['one']: 0x623: 1
    # d['two]: 0x633: 2
    # d['three']: 0x627: 3

# ### use case:
# user_data_list = ['Ivan', 'Ivanov', 23, 'Sofia']
# user_data_dict = {
#     'first name': 'Ivan',
#     'last name': 'Ivanov',
#     'age': 23,
#     'town': 'Sofia'
# }

# print(f'user age : {user_data_list[2]}')
# print(f'user age : {user_data_dict['age']}')


# example
# bg_en = {
#    'ябълка':'apple',
#    'портокал':'orange',
#    'ябълка':'strawberry',
# }

# print(bg_en)

# bg_word = 'ябълка'
# print( f'{bg_word}=> {bg_en[bg_word]}' )

# ------------------------------ Dict Operations ----------------------------- #
# l = [1,2,3]
# d = {
#     'one':1,
#     'two':2,
#     'three':3
# }

# Change item
# l[1] =  9
# d['one'] = 9

# add new item
# # l[3] = 9
# d['four'] = 4

# print(l)
# print(d)

# delete item
# del d['x']
# el = d.pop('x', 'Default')
# print(d)
# print(el)


# ------------------------------- Loop on dict ------------------------------- #
# d = {
#     'one':1,
#     'two':2,
#     'three':3
# }

### d.keys()
# keys = d.keys()
# for k in keys:
#     print( f'{k}-{d[k]}' )


# for k in d:
#      print( f'{k}-{d[k]}' )

### d.values()
# print( d.values() )

### d.items()
# print(d.items())
# for k,v in d.items():
#     print(f'{k}-{v}')


# TASK: print name of max scored student:
student_scores = {
    'Ivan': 5.00,
    'Alex': 8.50,
    'Maria': 5.50,
    'Georgy': 5.00
}

# max_score = max(student_scores.values())
# for name,score in student_scores.items():
#     if score==max_score:
#         print(f'{name} - {score}')

# print( student_scores['x'] )
# print( student_scores.get('x') )


# print( student_scores.get )
# print( student_scores.get('Alext') )


# def my_max(key):
#     print(f'key: {key}')
#     return student_scores[key]

# print( max(student_scores.keys(), key=my_max) )








