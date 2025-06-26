prices = ["$120", "$340", "$50", "$90"]

tozalangan_prices = list(map(lambda x : x.replace("$", ""),prices))

for price in tozalangan_prices:
    print(f"Narx: {price} som")
    


