import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# Generate a toy dataset
np.random.seed(0)
X = np.random.randn(20, 2)  # 20 random points in 2D space
y = np.array([1] * 10 + [-1] * 10)  # Labels: first 10 are 1, next 10 are -1
X[:10] += 1  # Shift class 1 to separate it from class -1
X[10:] -= 1  # Shift class -1 to separate it from class 1

# Create a function to plot SVM decision boundaries
def plot_svm_with_margin(C_value):
    # Train the SVM with a linear kernel and the given C value
    clf = svm.SVC(kernel='linear', C=C_value)
    clf.fit(X, y)

    # Create a grid of points to visualize decision boundary
    xx, yy = np.meshgrid(np.linspace(-3, 3, 500), np.linspace(-3, 3, 500))
    Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Plot the decision boundary and margins
    plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 7), cmap=plt.cm.PuBu)
    plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors='darkred')  # Decision boundary
    plt.contour(xx, yy, Z, levels=[-1, 1], linewidths=1, linestyles='--', colors='darkred')  # Margins

    # Plot data points
    plt.scatter(X[:, 0], X[:, 1], c=y, s=100, cmap=plt.cm.coolwarm)

    # Plot support vectors
    plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1],
                s=100, facecolors='darkgreen', edgecolors='k', label="Support Vectors", marker='^')

    plt.title(f"SVM with C = {C_value}")
    plt.legend()

# Plot for small C (allows more margin violations)
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plot_svm_with_margin(C_value=0.01)

# Plot for large C (strictly limits margin violations)
plt.subplot(1, 3, 2)
plot_svm_with_margin(C_value=1)

# Plot for large C (strictly limits margin violations)
plt.subplot(1, 3, 3)
plot_svm_with_margin(C_value=1000)

plt.tight_layout()
plt.show()