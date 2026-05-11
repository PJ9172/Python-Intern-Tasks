from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Load datasets
train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")

# Convert categorical data into numbers
train_df = pd.get_dummies(train_df, drop_first=True)
test_df = pd.get_dummies(test_df, drop_first=True)

# Remove unnecessary column
train_df = train_df.drop("Student_ID", axis=1)
test_df = test_df.drop("Student_ID", axis=1)

# Features and target
x_train = train_df.drop("Placement_Status_Placed", axis=1)
y_train = train_df["Placement_Status_Placed"]

x_test = test_df.drop("Placement_Status_Placed", axis=1)
y_test = test_df["Placement_Status_Placed"]

# Feature Scaling
scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

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