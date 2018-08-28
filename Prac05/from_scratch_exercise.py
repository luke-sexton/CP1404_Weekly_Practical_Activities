word_count = {}
text = input("Text: ")

words = text.split()
for word in words:
    occurence = word_count.get(word, 0)
    word_count[word] = occurence + 1


words = list(word_count.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_count[word]))