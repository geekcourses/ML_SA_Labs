input_str ='apple and banana one apple one banana a red apple and a green apple'

words_list = input_str.split(sep=' ')
# print(words_list)
words_count = dict()

for el in words_list:
	# if el is not in dict keys => d[el] = 1
	if el not in words_count.keys():
		words_count[el] = 1
	else:
		words_count[el] += 1

print( words_count )

