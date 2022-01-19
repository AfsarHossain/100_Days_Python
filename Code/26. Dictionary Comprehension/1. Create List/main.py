import random

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

# TODO: new_dict = {new_key:new_value for item in list}
students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)
# TODO: new_dict = {new_key:new_value for (key, value) in dictionary.items()}
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)
# TODO: new_dict = {new_key:new_value for (key, value) in dict.items() if test}
