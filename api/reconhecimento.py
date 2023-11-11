import cv2 as cv
import tensorflow as tf
import numpy as np

def model_prediction(test_image):
    model = tf.keras.models.load_model('fruit_vegetable_trained_model.h5')
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(224,224))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #Convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions) #Return index of max element

# result_index = model_prediction("Fruta.jpg")


