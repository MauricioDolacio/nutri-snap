import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import json

training_history = json.load(open('training_hist.json', 'r'))

print(training_history.keys())
print('Validation Accuracy: {} %'.format(training_history['val_accuracy'][-1]*100))

epochs = [i for i in range(1,37)]
plt.plot(epochs,training_history['accuracy'],color='red')
plt.xlabel('Number of Epochs')
plt.ylabel('Training Accuracy')
plt.title('Visualization of Training Accuracy Result')
plt.show()

plt.plot(epochs, training_history['val_accuracy'], color='blue')
plt.xlabel('Number of Epochs')
plt.ylabel('Validation Accuracy')
plt.title('Visualization of Validation Accuracy Result')
plt.show()
