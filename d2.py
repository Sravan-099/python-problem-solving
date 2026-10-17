d1 = {"apple": 10, "banana": 20, "mango": 30}
d2 = {"apple": 5, "banana": 15, "orange": 25}
d3 = d1.copy()

for key, value in d2.items():
    if key in d3:
        d3[key] += value
    else:
        d3[key] = value

print(d3)