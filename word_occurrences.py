string = "this is a collection of words of nice words this is a fun thing it is"
print(f"Text: {string}")

words_count = {}

for words in string.split():
    if words not in words_count:
        words_count[words] = 0
    words_count[words] += 1

for words in sorted(words_count):
    print(f"{words:12}: {words_count[words]}")