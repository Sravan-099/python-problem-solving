numbers = [10, -5, 0, 8, -3, 0, 10, -5]
positive = {}
negative = {}
zero = {}
for num in numbers:
    if num > 0:
        positive[num] = positive.get(num, 0) + 1
    elif num < 0:
        negative[num] = negative.get(num, 0) + 1
    else:
        zero[num] = zero.get(num, 0) + 1
print(positive)
print(negative)
print(zero)