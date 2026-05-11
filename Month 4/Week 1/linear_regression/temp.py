from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import pandas as pd

# Load datasets
df = pd.read_csv("D:\\Prajwal\\Python Tasks\\Month 4\\Week 1\\linear_regression\\Ice Cream Sales - temperatures.csv")
print("Loading Dataset :\n",df.head())

# feature (input)
x = df[["Temperature"]]

# target (output)
y = df["Ice Cream Profits"]

x_train, xtest, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Model
model = LinearRegression()

# Train
model.fit(x_train, y_train)

# Predictions
predictions = model.predict(xtest)

# Evaluation
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
# Results
print(f"\nMean Squared Error: {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")

# Predict new data
new_temperature = pd.DataFrame({
    "Temperature": [30]
})
predicted_profit = model.predict(new_temperature)
print(f"\nPredicted Ice Cream Profit for Temperature = 30: {predicted_profit[0]:.2f}")
