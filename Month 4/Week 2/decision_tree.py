from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt

# Load the Iris dataset
iris = load_iris() 
x = iris.data
y = iris.target

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Create a Decision Tree Classifier
# we will set max_depth to 3 to prevent overfitting
model = DecisionTreeClassifier(max_depth=3, criterion='gini')

# Train the model
model.fit(x_train, y_train)

# Make predictions on the test set
predictions = model.predict(x_test)
print(f"Model Accuracy: {accuracy_score(y_test, predictions) * 100:.2f}%")

# Visualize the Decision Tree
plt.figure(figsize=(12, 8))
plot_tree(model, filled=True, feature_names=iris.feature_names, class_names=iris.target_names)
plt.title("Decision Tree Visualization")
plt.show()