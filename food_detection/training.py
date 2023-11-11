# Importação de bibliotecas necessárias
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

# Definição de parâmetros
batch_size = 16
img_height = 224
img_width = 224

TEST_DIR = 'test'
TRAIN_DIR ='train'
VALID_DIR ='validation'

# Pré-processamento e Segmentação
# Carregamento dos dados de treino, validação e teste usando o TensorFlow Dataset API
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    TRAIN_DIR,
    seed=2509,
    image_size=(img_height, img_width),
    batch_size=batch_size
)

valid_ds = tf.keras.preprocessing.image_dataset_from_directory(
    VALID_DIR,
    seed=2509,
    image_size=(img_height, img_width),
    shuffle=False,
    batch_size=batch_size
)

test_ds = tf.keras.preprocessing.image_dataset_from_directory(
    TEST_DIR,
    seed=2509,
    image_size=(img_height, img_width),
    shuffle=False,
    batch_size=batch_size
)

# Descrição
# Visualização de algumas imagens do conjunto de treino
class_names = train_ds.class_names
print(class_names)

plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(class_names[labels[i]])
        plt.axis("off")

# Representação
# Carregamento de um modelo de base pre-treinado (MobileNetV2)
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(224,224,3),
    include_top=False,
    weights='imagenet'
)

base_model.trainable = False

# Data Augmentation
# Adição de camadas de pré-processamento e aumento de dados ao modelo
data_augmentation = tf.keras.Sequential([
    tf.keras.layers.experimental.preprocessing.RandomFlip("horizontal"),
    tf.keras.layers.experimental.preprocessing.RandomRotation(0.2),
    tf.keras.layers.experimental.preprocessing.RandomZoom(0.2),
])

# Construção do modelo
inputs = tf.keras.Input(shape=(224,224,3))
x = tf.keras.layers.experimental.preprocessing.Rescaling(1./255)(inputs)
x = data_augmentation(x)
x = base_model(x,training=False)
x = tf.keras.layers.GlobalAveragePooling2D()(x)
x = tf.keras.layers.Flatten()(x)
x = tf.keras.layers.Dense(1024,activation='relu')(x)
x = tf.keras.layers.Dense(512,activation='relu')(x)
x = tf.keras.layers.Dense(len(class_names),activation='softmax')(x)

model = tf.keras.Model(inputs=inputs, outputs=x, name="trained_model")

# Compilação do modelo
model.compile(
    loss = tf.keras.losses.SparseCategoricalCrossentropy(),
    optimizer = tf.keras.optimizers.Adam(lr=0.001),
    metrics = ["accuracy"]
)

# Treinamento
# Treinamento inicial do modelo
initial_epochs = 5

history = model.fit(
    x=train_ds,
    epochs= initial_epochs,
    validation_data=valid_ds
)

# Visualização de métricas de treinamento
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.plot(acc, label='Training Accuracy')
plt.plot(val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.ylabel('Accuracy')
plt.ylim([min(plt.ylim()),1])
plt.title('Training and Validation Accuracy')

plt.subplot(2, 1, 2)
plt.plot(loss, label='Training Loss')
plt.plot(val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.ylabel('Cross Entropy')
plt.title('Training and Validation Loss')
plt.xlabel('epoch')
plt.show()

# Fine-tuning
# Liberação de camadas do modelo base para fine-tuning
base_model.trainable = True

# Compilação do modelo para fine-tuning
model.compile(
    loss = tf.keras.losses.SparseCategoricalCrossentropy(),
    optimizer = tf.keras.optimizers.Adam(1e-5),
    metrics = ["accuracy"]
)

# Fine-tuning
fine_tune_epochs = 5
total_epochs =  initial_epochs + fine_tune_epochs

history_fine = model.fit(
    train_ds,
    epochs=total_epochs,
    initial_epoch=history.epoch[-1],
    validation_data=valid_ds
)

# Visualização de métricas após fine-tuning
acc += history_fine.history['accuracy']
val_acc += history_fine.history['val_accuracy']

loss += history_fine.history['loss']
val_loss += history_fine.history['val_loss']

plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.plot(acc, label='Training Accuracy')
plt.plot(val_acc, label='Validation Accuracy')
plt.ylim([0.0, 1])
plt.plot([initial_epochs-1,initial_epochs-1],
plt.ylim(), label='Start Fine Tuning')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(2, 1, 2)
plt.plot(loss, label='Training Loss')
plt.plot(val_loss, label='Validation Loss')
plt.plot([initial_epochs-1,initial_epochs-1],
plt.ylim(), label='Start Fine Tuning')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.xlabel('epoch')
plt.show()

# Avaliação do modelo no conjunto de teste
model.evaluate(test_ds)

# Predições e Salvamento do modelo
predictions = model.predict(valid_ds, verbose=1)
predictions.shape

np.sum(predictions[0])
predictions[0]

class_names[np.argmax(predictions[0])]

score = tf.nn.softmax(predictions[0])
score

model.save("trained_model.h5")
np.save('class_names.npy',class_names)
