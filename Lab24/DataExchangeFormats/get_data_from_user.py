def write_to_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

# write_to_file('userdata.txt', 'Ada', 34)

content = ''
for _ in range(3):
    user_name=input('Enter name:')
    user_age=input('Enter age:')
    content+=f'{user_name},{user_age}\n'

print(content)
write_to_file('userdata.txt',content )