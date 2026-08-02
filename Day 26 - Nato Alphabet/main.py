
# # old_list = [1,2,3]
# # new_list = [item + 1  for item in old_list] 

# # print(new_list)

# new_list = [item * 2 for item in range(1,5)]

# print(new_list)

import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']  

students_score = {student:random.randint(1,100) for student in names}

passed_students = {student:score for (student, score) in students_score.items() if score >= 50}

print(passed_students)

