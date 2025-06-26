

votes = [
  {"option": "A", "votes": 123},
  {"option": "B", "votes": 145},
  {"option": "C", "votes": 97}
]
eng_kop_toplagan =max(votes, key=lambda x: x["votes"])
print(f"eng Kop toplagan ovoz {eng_kop_toplagan}")