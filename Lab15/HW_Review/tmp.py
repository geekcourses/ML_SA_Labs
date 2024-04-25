city_distances = [
    ["Bansko", 97],
    ["Brussels", 1701],
    ["Alexandria", 1403],
    ["Nice", 1307],
    ["Szeged", 469],
    ["Dublin", 2479],
    ["Palermo", 987],
    ["Moscow", 1779],
    ["Oslo", 2098],
    ["London", 2019],
    ["Madrid", 2259]
]


### Variant 1
# filtered_cities = []
# for city_distance in city_distances:
#     if city_distance[1] < 1500:
#         filtered_cities.append([city_distance[0], city_distance[1]])


### Variant 2
filtered_cities = [cd for cd in city_distances if cd[1]<1500]
print(filtered_cities)

