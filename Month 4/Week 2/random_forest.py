from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

# Load data
data = load_iris()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Forest
# n_estimators = number of trees in the forest
rf_clf = RandomForestClassifier(n_estimators=100, max_depth=3, random_state=42)

# Train and Predict
rf_clf.fit(X_train, y_train)
preds = rf_clf.predict(X_test)

print(f"Random Forest Accuracy: {accuracy_score(y_test, preds) * 100:.2f}%")