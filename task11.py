nums = list(range(1, 21))

juft_son = filter(lambda son : son % 2 ==0 , nums)

kvatrat = list(map(lambda son : son ** 2 , juft_son))
print(kvatrat)