import pickle
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Load sample data
X, y = load_iris(return_X_y=True)

# Train model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Save model correctly
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
