student_dict = {
    "student": ["Angela", "James", "Lily"],
    "scores": [56, 76, 98]
}

# TODO: Looping through dictionaries
# for (key, value) in student_dict.items():
#     # print(key)
#     print(value)

# TODO: Using Pandas

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# TODO: Loop through a data frame
# for (key, value) in student_data_frame.items():
#     # print(key)
#     print(value)

# TODO: Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    # print(row.student)
    # print(row.scores)
    if row.student == "Angela":
        print(row.scores)
