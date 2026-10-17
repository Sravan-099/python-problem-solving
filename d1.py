highest = 0
name = ""

for student, marks in students.items():
    total = 0
    for subject, mark in marks.items():
        total += mark
    if total > highest:
        highest = total
        name = student

print(name, highest)