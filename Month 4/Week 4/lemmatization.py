from nltk.stem import WordNetLemmatizer, PorterStemmer
# import nltk
# nltk.download('wordnet')

ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()


print(lemmatizer.lemmatize("better", pos='a'))  # Adjective
print(lemmatizer.lemmatize("running", pos='v'))  # Verb
print(lemmatizer.lemmatize("cats", pos='n'))     # Noun

words = ["running", "flies", "better", "cats", "studies"]

print("Stemmed Words: ")
for word in words:
    stem = ps.stem(word)
    print(f"{word} -> {stem}")


print("\nLemmatized Words: ")
for word in words:
    lemma = lemmatizer.lemmatize(word)
    print(f"{word} -> {lemma}")