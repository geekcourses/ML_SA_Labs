# --------------------------- filter_city_distances -------------------------- #
# city_distances = [
#     ["Bansko", 97],
#     ["Brussels", 1701],
#     ["Alexandria", 1403],
#     ["Nice", 1307],
#     ["Szeged", 469],
#     ["Dublin", 2479],
#     ["Palermo", 987],
#     ["Moscow", 1779],
#     ["Oslo", 2098],
#     ["London", 2019],
#     ["Madrid", 2259]
# ]


# ### Variant 1
# # filtered_cities = []
# # for city_distance in city_distances:
# #     if city_distance[1] < 1500:
# #         filtered_cities.append([city_distance[0], city_distance[1]])


# ### Variant 2
# filtered_cities = [cd for cd in city_distances if cd[1]<1500]
# print(filtered_cities)


# ------------------------ merge_and_capitalize_names ------------------------ #
# first_names = ["ivan", "maria", "petar"]
# sur_names = ["ivanov", "popova", "petrov"]

# full_names = []
# # for idx,name  in enumerate(first_names):
# for idx  in range(0, len(first_names)):
#     # full_names.append( first_names[idx].capitalize() + " " + sur_names[idx].capitalize())
#     full_names.append( f'{first_names[idx].capitalize()} {sur_names[idx].capitalize()}')


# # full_names = [
# #     name.capitalize() + " " + sur_names[idx].capitalize()
# #     for idx,name  in enumerate(first_names)
# # ]
# print(full_names)

# --------------------------- best_students_scores --------------------------- #
student_scores = [
    ['Ivan', 5.00],
    ['Alex', 3.50],
    ['Maria', 5.50],
    ['Georgy', 5.00]
]



best_students_scores = [sc for sc in student_scores if sc[1]>4]

for sc in student_scores:
    print(f'{sc[0].ljust(8, ' ')} - {sc[1]}')
    # print(f'{sc[0]:<8s} - {sc[1]}')