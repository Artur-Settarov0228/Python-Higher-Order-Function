data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]
faqat_string = list(filter(lambda x: isinstance(x, str), data))

uzunligi = sorted(faqat_string, key=lambda x: len(x))
print(uzunligi)
