import tensorflow as tf
import numpy as np

def model_prediction(test_image):
    model = tf.keras.models.load_model('trained_model.h5', compile=False)
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(224,224))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #Convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions) #Return index of max element

image = 'test/tomato/Image_6.jpg'
result_index = model_prediction(image)

with open('labels.txt') as f:
    content = f.readlines()
label = []
for i in content:
    label.append(i[:-1])

print(label[result_index])
