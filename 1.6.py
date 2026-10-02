words = ["apple", "banana", "kiwi", "pear"]

short_words = list(filter(lambda word: len(word) <= 4, words))

print(short_words)
