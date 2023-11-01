import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


training_set = tf.keras.utils.image_dataset_from_directory(
    'train',
    labels= 'inferred',
    label_mode = 'categorical',
    class_names = None,
    color_mode ='rgb',
    batch_size = 16,
    image_size = (512,512),
    shuffle = True,
    seed = None,
    validation_split = None,
    subset = None,
    interpolation = 'bilinear',
    follow_links = False,
    crop_to_aspect_ratio = False,
)

validation_set = tf.keras.utils.image_dataset_from_directory(
    'validation',
    labels = 'inferred',
    label_mode = 'categorical',
    class_names = None,
    color_mode ='rgb',
    batch_size = 16,
    image_size = (512,512),
    shuffle = True,
    seed = None,
    validation_split = None,
    subset = None,
    interpolation = 'bilinear',
    follow_links = False,
    crop_to_aspect_ratio = False
)

cnn = tf.keras.models.Sequential()

cnn.add(tf.keras.layers.Conv2D(filters=32,kernel_size=3,activation='relu', input_shape=[512,512,3]))
cnn.add(tf.keras.layers.Conv2D(filters=32,kernel_size=3,activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2,strides=2))

cnn.add(tf.keras.layers.Conv2D(filters=64,kernel_size=3,activation='relu'))
cnn.add(tf.keras.layers.Conv2D(filters=64,kernel_size=3,activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2,strides=2))

cnn.add(tf.keras.layers.Flatten())
cnn.add(tf.keras.layers.Dense(units=512,activation='relu'))
cnn.add(tf.keras.layers.Dense(units=512,activation='relu'))
cnn.add(tf.keras.layers.Dropout(0.5))
cnn.add(tf.keras.layers.Dense(units=36,activation='softmax'))

cnn.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
cnn.summary()

training_history = cnn.fit(x=training_set, validation_data=validation_set, epochs=36, batch_size=16)

cnn.save('trained_model.h5')

training_history.history #Return dictionary of history

#Saving History in JSON
import json
with open('training_hist.json', 'w') as f:
  json.dump(training_history.history,f)

print(training_history.history.keys())

print('Validation Accuracy: {} %'.format(training_history.history['val_accuracy'][-1]*100))

epochs = [i for i in range(1,33)]
plt.plot(epochs,training_history.history['accuracy'],color='red')
plt.xlabel('Number of Epochs')
plt.ylabel('Training Accuracy')
plt.title('Visualization of Training Accuracy Result')
plt.show()

plt.plot(epochs, training_history.history['val_accuracy'], color='blue')
plt.xlabel('Number of Epochs')
plt.ylabel('Validation Accuracy')
plt.title('Visualization of Validation Accuracy Result')
plt.show()

training_loss, training_accuracy = cnn.evaluate(training_set)

val_loss, val_accuracy = cnn.evaluate(validation_set)

test_set = tf.keras.utils.image_dataset_from_directory(
    'test',
    labels= 'inferred',
    label_mode = 'categorical',
    class_names = None,
    color_mode ='rgb',
    batch_size = 32,
    image_size = (512,512),
    shuffle = True,
    seed = None,
    validation_split = None,
    subset = None,
    interpolation = 'bilinear',
    follow_links = False,
    crop_to_aspect_ratio = False,
)

test_loss, test_accuracy = cnn.evaluate(test_set)