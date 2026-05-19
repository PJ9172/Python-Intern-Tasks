from nltk.stem import PorterStemmer

ps = PorterStemmer()
print(ps.stem("running"))

words = ["running", "flies", "better", "cats", "studies"]

print("Stemmed Words: ")
for word in words:
    stem = ps.stem(word)
    print(f"{word} -> {stem}")

