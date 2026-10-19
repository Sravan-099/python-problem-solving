data = {"a": 10, "b": 20, "c": 10, "d": 30, "e": 20, "f": 40}
seen = []
duplicates = []
for value in data.values():
    if value in seen:
        if value not in duplicates:
            duplicates.append(value)
    else:
        seen.append(value)
print(duplicates)