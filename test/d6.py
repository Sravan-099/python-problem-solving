marks = {"A": 80, "B": 35, "C": 90, "D": 45}
result = {}

for key, value in marks.items():
    if value >= 50:
        result[key] = value

print(result)