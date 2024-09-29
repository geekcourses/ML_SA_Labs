# Import necessary libraries
from keras.models import Sequential
from keras.layers import Input, Dense

from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# Example dataset creation
X, y = make_classification(n_samples=1000, n_features=8, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize a Sequential model
model = Sequential()

# Add an Input layer with 8 features (input shape)
model.add(Input(shape=(8,)))
# Add a Dense hidden layer with 32 neurons and ReLU activation
model.add(Dense(32, activation='relu'))
# Add the output layer with 1 neuron and sigmoid activation for binary classification
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model on the training data (X_train, y_train)
model.fit(X_train, y_train, epochs=10, batch_size=32)

