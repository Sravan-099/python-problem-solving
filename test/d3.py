numbers = [1, 2, 3, 2, 1, 4, 2, 3, 1]
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)