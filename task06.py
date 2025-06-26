def is_email(email):
    a = str(email)
    return a.endswith("@gmail.com")

emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]

saralangan_email = list(filter(is_email, emails))
print(saralangan_email)