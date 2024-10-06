import os
import cv2
import tensorflow as tf
from keras.layers import TFSMLayer
from tensorflow.keras.layers import DepthwiseConv2D

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

print("TensorFlow version:", tf.__version__)
print(os.getcwd())

#Load image
image = cv2.imread('./c10afe7519.jpg')
print(image.shape)

#Reshape image


#Load model
# model = tf.keras.models.load_model('./keras_model.h5')

try:
    model = tf.keras.models.load_model('./keras_model.h5', custom_objects={'DepthwiseConv2D': DepthwiseConv2D})
except:
    model = TFSMLayer('./keras_model.h5', call_endpoint='serving_default')
