# Nutri Snap
Nutri Snap is an application that shows the nutritional values of a food with just a photo.

![NutriSnap](https://imgur.com/DtqG8hZ.jpg)


## Overview

The application allows the user to take/send photos of fruits and vegetables and returns the nutritional values of the food. To recognize food, an image classification model was trained to identify around 36 fruits and vegetables with an accuracy of 94%.

- **/api:** Backend. Food recognition and research into nutritional values.
- **/flutter:** Mobile Application.
- **/food_detection:** Fruit and vegetable classifier training files.

## Prerequisites
- [Python Install](https://www.python.org/downloads/)
- [Flutter Install](https://docs.flutter.dev/get-started/install)

Run in Terminal:
```
pip install tensorflow
pip install flask
```

## Installation
[Download Trained Model Here](https://drive.google.com/drive/folders/1KEwf_s9SDkonnZNCiyxEs7PFO6u3T8cj?usp=drive_link)

- Copy the project. OBS: '/food_detection' is not necessary
- Download and insert the model 'fruit_and_vegetable_trained_model.h5' to the folder '/api'
- In '/api' run 'main.py' to start the Backend API
- In '/flutter' run 'main.dart' file to start the application

##  Tools Used
- [Tensorflow](https://www.tensorflow.org/)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Edamam API](https://www.edamam.com/)

## Credits
[Kritik Seth, "Fruits and Vegetables Image Recognition Dataset," Kaggle 2020](https://www.kaggle.com/kritikseth/fruit-and-vegetable-image-recognition)
