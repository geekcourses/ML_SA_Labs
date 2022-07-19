student_scores = {
	'Ivan'  : 5.00,
	'Alex'  : 3.50,
	'Maria' : 5.50,
	'Georgy': 5.00
}

scores_list = list(student_scores.values())
names_list = list(student_scores.keys())

max_score = max(scores_list)

max_score_index = scores_list.index(max_score)

print(f'{names_list[max_score_index]} has max score: {max_score}')

