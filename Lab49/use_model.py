import cv2
import tensorflow as tf
import os

print(os.getcwd())

# Load image
image_to_predict = cv2.imread('./test_image.png',  cv2.IMREAD_GRAYSCALE)
print(image_to_predict.shape)

# Reshape
image_to_predict_reshaped = image_to_predict.reshape(1,28*28)


# Load model
model = tf.keras.models.load_model('./models/digit_recognition_model.keras')

probs = model.predict(image_to_predict_reshaped)
result = probs.argmax()

print(probs)
print(result)
