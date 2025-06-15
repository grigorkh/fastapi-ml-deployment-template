from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
import os

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Ensure output directory exists
os.makedirs("model", exist_ok=True)

# Save model
with open("model/iris_model.pkl", "wb") as f:
    pickle.dump(clf, f)

print("✅ Model trained and saved to model/iris_model.pkl")
