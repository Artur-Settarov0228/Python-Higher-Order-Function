def alohida_raqam(raqam:str):
    return raqam.isdigit()

text = ["apple", "34", "banana", "100", "abc", "75"]
result = list(filter(alohida_raqam,text))
print(result)