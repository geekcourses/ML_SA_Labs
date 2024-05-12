# TV,   Radio,Newspaper,Sales
# 230.1, 37.8,  69.2, 22.1
# 44.5,  39.3,  45.1, 10.4
# 17.2,  45.9,  69.3, 12


# ad_dict = {
#     'TV': [ 230.1, 44.5, 17.2],
#     'Radio': [ 37.8, 39.3, 45.9],
#     'Newspaper': [ 69.2, 45.1, 69.3],
#     'Sales': [ 22.1, 10.4, 12]
# }

# for el in ad_dict['TV']:
#     print(el)


# ad_headers = [ 'TV', 'Radio', 'Newspaper', 'Sales']
# ad_data = [
#     [230.1, 37.8, 69.2, 22.1],
#     [44.5, 39.3, 45.1, 10.4],
#     [17.2, 45.9, 69.3, 12]
# ]


# TASK: print all values in column 'Sales' in ad_data
# get index of 'TV'
# tv_idx = ad_headers.index('Sales')
# print(tv_idx)

# for el in ad_data:
#     # el = [230.1, 37.8, 69.2, 22.1],
#     print(el[tv_idx])


ages= [10, 20, 25, 30, 35]
ages_normalized = []
for el in ages:
    ages_normalized.append(el/10)

print(ages_normalized)

# import numpy as np

# ages = np.array( [10, 20, 25, 30, 35] )
# ages_normalized = ages/10;
# print(ages_normalized)