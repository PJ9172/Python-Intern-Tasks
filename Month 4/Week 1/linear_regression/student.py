from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

# Load datasets
df = pd.read_csv("D:/Prajwal/Python Tasks/Month 4/Week 1/linear_regression/StudentsPerformance.csv")
print("Loading Dataset :\n",df.head())

# feature (input)
x = df[["reading score", "writing score"]]

# target (output)
y = df["math score"]

# Split Dataset
x_train, xtest, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Model
modle = LinearRegression()

# Train
modle.fit(x_train, y_train)

# Predictions
predictions = modle.predict(xtest)

# Evaluation    
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

# Results
print(f"\nMean Squared Error: {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")

# Predict new data
new_student = pd.DataFrame({
    "reading score": [85],
    "writing score": [90]
})
predicted_math_score = modle.predict(new_student)
print(f"\nPredicted Math Score for reading_score=85 and writing_score=90: {predicted_math_score[0]:.2f}")