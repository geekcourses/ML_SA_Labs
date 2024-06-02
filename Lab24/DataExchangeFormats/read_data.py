def read_from_file(filename):
    with open(filename, 'r') as f:
        return f.read()


data = []
content = read_from_file('userdata.csv')
print(content)

lines = content.split('\n')
lines.pop(-1)
print(lines)
for line in lines:
    name, age = line.split(',')
    data.append((name,age))







print(data)


# data = [
#     ('Ada', 34),
#     ('Pesho', 27),
#     ('Pesho', 27),
# ]

