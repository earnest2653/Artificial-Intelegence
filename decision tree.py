from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

# Load the Iris dataset (a built-in dataset in scikit-learn)
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Create a Decision Tree classifier
clf = DecisionTreeClassifier()

# Train the classifier on the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
predictions = clf.predict(X_test)

# Display the accuracy of the classifier on the test data
accuracy = clf.score(X_test, y_test)
print(f"Accuracy: {accuracy}")

# Display the Decision Tree rules
tree_rules = export_text(clf, feature_names=iris.feature_names)
print("Decision Tree Rules:")
print(tree_rules)
