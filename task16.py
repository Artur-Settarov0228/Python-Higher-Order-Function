data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]
uzunligi = sorted(data, key=lambda x : len(str(x)))
print(uzunligi)
