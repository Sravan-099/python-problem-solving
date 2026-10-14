numbers = [12, 45, 7, 89, 23]
smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest:", smallest)
