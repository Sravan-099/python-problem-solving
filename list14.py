numbers = [12, 45, 7, 89, 23]
smallest = numbers[0]
for n in numbers:
    if n < smallest:
        smallest = n
print("Smallest element:", smallest)