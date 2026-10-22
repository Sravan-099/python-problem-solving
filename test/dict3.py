stock = {
    "apples": 34,
    "bananas": 12,
    "oranges": 57,
    "grapes": 8,
    "mangoes": 23
}

lowest = min(stock, key=stock.get)

print("Lowest stock item:", lowest)