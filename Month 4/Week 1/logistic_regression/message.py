from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.model_selection import train_test_split

# Loading dataset
df = pd.read_csv("D:\\Prajwal\\Python Tasks\\Month 4\\Week 1\\logistic_regression\\spam.csv", encoding="latin-1")
print("Loading Data :\n",df.head())

# Initialize CountVectorizer
vectorizer = CountVectorizer()

# keep only needed columns
df = df[["v1","v2"]]

# Rename columns
df = df.rename(columns={"v1": "label", "v2": "message"})

# Convert lables into numbers
df["label"] = df["label"].map({"ham": 0, "spam": 1})

# Features and target
x = df["message"]
y = df["label"]

# Convert text data into numbers using CountVectorizer
x = vectorizer.fit_transform(x)

# Split Dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Model
model = LogisticRegression(max_iter=2000)

# Train
model.fit(x_train, y_train)

# Predictions
predictions = model.predict(x_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)
print(f"\nModel Accuracy: {accuracy:.2f}")

# Full Report
print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Predict new data
new_message = ["Congratulations! You've won a free ticket to the Bahamas! Call now to claim your prize."]
new_message_vectorized = vectorizer.transform(new_message)

predictions = model.predict(new_message_vectorized)
if predictions[0] == 1:
    print("\nThe message is classified as: SPAM")
else:
    print("\nThe message is classified as: HAM")