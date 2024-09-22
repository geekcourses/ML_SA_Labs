import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# Create dataset
X = np.array([[1, 2], [2, 3], [3, 3], [5, 6], [6, 7], [7, 8]])
y = [0, 0, 0, 1, 1, 1]

# Fit the SVM model
model = svm.SVC(kernel='linear')
model.fit(X, y)

# Plot data points
plt.scatter(X[:, 0], X[:, 1], c=y)

# Extract model parameters
w = model.coef_[0]
b = model.intercept_[0]

# Compute the decision boundary
x_min, x_max = X[:, 0].min(), X[:, 0].max()  # Use min and max of X values
x_plot = np.array([x_min, x_max])
y_plot = -(w[0] * x_plot + b) / w[1]

plt.show()