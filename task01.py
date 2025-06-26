def musbat_son(num):
    return num > 0

numbers = [4, -2, 0, 7, -9, 3, -1, 5]

result = list(filter(musbat_son, numbers))

print(result)
