import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# # Download required datasets (run once)
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('punkt_tab')

# Sample sentence
text = "This is a simple demonstration of removing stopwords from a sentence."

# Tokenize sentence into words
words = word_tokenize(text)

# Load English stopwords
stop_words = set(stopwords.words('english'))

# Remove stopwords
filtered_words = [word for word in words if word.lower() not in stop_words]

# Output
print("Original Words:")
print(words)

print("\nAfter Removing Stopwords:")
print(filtered_words)