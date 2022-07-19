# student_scores = [
# 	('Ivan'  , [5.00, 4.50, 3.50]),
# 	('Alex'  , 3.50),
# 	('Maria' , 5.50),
# 	('Georgy', 5.00)
# ]

student_scores = {
	'Ivan'  : 5.00,
	'Alex'  : 3.50,
	'Maria' : 5.50,
	'Georgy': 5.00
}

best_students_scores = dict()

for key, val in student_scores.items():
	if val > 4.00:
		best_students_scores[key] = val


for k,v in best_students_scores.items():
	print(f'{k} {val:.2f}')

# text = '''
# 	   apple and banana one apple one banana
# 	   a red apple and a green apple
# 	   '''

# print('\n')
# print('\n')


# words_list = text.split()
# new_set = set(sorted(words_list, key=len, reverse=False))

# for x in new_set:
# 	print(x,words_list.count(x))

# test = {'Ivan'  : 5.00,
# 		'Alex'  : 3.50,
# 		'Maria' : 5.50,
# 		'Georgy': 5.00}