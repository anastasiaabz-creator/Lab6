words = input().lower().split()
word_counts = {}

for word in set(words):
    word_counts[word] = words.count(word)

for word, count in word_counts.items():
    print(word, count)

