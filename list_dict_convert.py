
students = [
    (1, "Junak", "A"),
    (2, "Manas", "B"),
    (3, "Paras", "A"),
    (4, "Pranoy", "C"),
    (5, "Raj", "B")
]


students_dict = {student[0]: {"name": student[1], "grade": student[2]} for student in students}


print("Students dictionary:")
print(students_dict)
