data = {"a": 1, "b": 2, "c": 3}
result = {}

for key, value in data.items():
    result[value] = key

print(result)