# dev1 = {
#     'name': 'Petar',
#     'age': 23,
#     'salary': 4000,
#     'skills': ['Python', 'ML']
# }

# dev2 = {
#     'name': 'Maria',
#     'age': 34,
#     'salary': 5000,
#     'skills': ['JS', 'Node', 'React']
# }


devs = []
for entry in range(3):
    dev = {
        'name' : input('Enter name: '),
        'age' : int(input('Enter age: ')),
        'salary' : int(input('Enter salary: ')),
        'skills' : input('Enter skills: ').split(',')
    }
    devs.append(dev)





