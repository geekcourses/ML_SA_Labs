from sklearn.datasets import make_circles
from sklearn.svm import SVC
import matplotlib.pyplot as plt

# Create circular data
X, y = make_circles(n_samples=100, factor=.3, noise=.05)

# Fit SVM with RBF kernel
clf = SVC(kernel='rbf')
clf.fit(X, y)

# Plot data and decision boundary
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()