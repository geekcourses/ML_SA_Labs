# TASK:
#     user will enter next information:
#         student | score
#         Maria   | 5
#         Pesho   | 4
#         Ivan    | 6

#     print the name of the student with max score


### Get students data
# students = []
# scores = []
# for el in range(3):
#     student = input('Enter student: ')
#     score = int(input('Enter score: '))

#     students.append(student)
#     scores.append(score)

# print(students)
# print(scores)

students = ['Maria', 'Pesho', 'Ivan']
scores = [5,4,3]

### Find max score index
max_score_idx = scores.index( max(scores) )
print(max_score_idx)

### Print the name of the student with max score
print(students[max_score_idx])
