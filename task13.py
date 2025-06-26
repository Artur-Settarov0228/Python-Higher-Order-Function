
sentence = "Functional programming in Python is very powerful and elegant"
words = sentence.split()
sorted_word = sorted(words, key=lambda word :len(word) ,reverse=True)

top_3_words = sorted_word[:3]
print(top_3_words)