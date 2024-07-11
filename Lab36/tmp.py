import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, RegressorMixin
import matplotlib.pyplot as plt

class LinearRegressionGD(BaseEstimator, RegressorMixin):
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations

    def fit(self, X, y):
        X_b = np.c_[np.ones((X.shape[0], 1)), X]  # add x0 = 1 to each instance
        self.theta_ = np.random.randn(X_b.shape[1], 1)  # random initialization
        m = len(y)

        for _ in range(self.n_iterations):
            gradients = 2/m * X_b.T.dot(X_b.dot(self.theta_) - y)
            self.theta_ -= self.learning_rate * gradients
        return self

    def predict(self, X):
        X_b = np.c_[np.ones((X.shape[0], 1)), X]  # add x0 = 1 to each instance
        return X_b.dot(self.theta_)

# Load the data
file_path = 'https://raw.githubusercontent.com/geekcourses/JupyterNotebooksExamples/master/Notebooks/supervised_learning_algorihtms/linear_models_for_classification_and_regression/SimpleLinearRegression/Salary_Data.csv'

# Importing the dataset
data = pd.read_csv(file_path)

X = data[['YearsExperience']].values
y = data[['Salary']].values

print(X.shape)
print(y.shape)

# Create and fit the model
model = LinearRegressionGD(learning_rate=0.01, n_iterations=1000)
model.fit(X, y)

# Predict using the model
y_pred = model.predict(X)

# Print the coefficients
print(f"Intercept: {model.theta_[0][0]}")
print(f"Coefficient: {model.theta_[1][0]}")

# Plot the results
plt.plot(X, y, "b.")
plt.plot(X, y_pred, "r-")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Linear Regression with Gradient Descent on Salary Data")
plt.show()
