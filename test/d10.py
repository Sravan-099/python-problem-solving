students = {
    "Sravan": {"Python": 85, "Java": 90},
    "Rahul": {"Python": 95, "Java": 88},
    "Anil": {"Python": 78, "Java": 82}
}
highest = 0
name = ""
for student, marks in students.items():
    total = 0
    for mark in marks.values():
        total += mark
    if total > highest:
        highest = total
        name = student
print(name, highest)