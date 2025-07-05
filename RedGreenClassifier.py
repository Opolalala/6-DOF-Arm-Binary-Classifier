import os
import tensorflow as tf
import numpy as np
import zipfile
import matplotlib.pyplot as plt
import serial
import time

with zipfile.ZipFile("dataset.zip", 'r') as zip_ref:
    zip_ref.extractall()

dataset_dir = "dataset"
red_dir = os.path.join(dataset_dir, 'red')
green_dir = os.path.join(dataset_dir, 'green')

model = tf.keras.models.Sequential([
    tf.keras.Input(shape=(360, 640, 3)),
    tf.keras.layers.Conv2D(16, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),

    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy',
              optimizer=tf.keras.optimizers.RMSprop(learning_rate=0.001),
              metrics=['accuracy'])

train_dataset = tf.keras.utils.image_dataset_from_directory(
    dataset_dir,
    image_size=(360, 640),
    batch_size=32,
    label_mode='binary'
    )

rescale_layer = tf.keras.layers.Rescaling(scale=1./255)
def rescale_image(image, label):
     return rescale_layer(image), label

train_dataset_scaled = train_dataset.map(rescale_image)

SHUFFLE_BUFFER_SIZE = 1000
PREFETCH_BUFFER_SIZE = tf.data.AUTOTUNE

train_dataset_final = (train_dataset_scaled
                       .cache()
                       .shuffle(SHUFFLE_BUFFER_SIZE)
                       .prefetch(PREFETCH_BUFFER_SIZE)
                      )
history = model.fit(
    train_dataset_final,
    epochs=15,
    verbose=2
    )

def predict_image(img_path):
    image = tf.keras.utils.load_img(img_path, target_size=(360, 640))
    image_array = tf.keras.utils.img_to_array(image)
    image_array = rescale_layer(image_array)
    image_array = np.expand_dims(image_array, axis=0)

    prediction = model.predict(image_array, verbose=0)[0][0]

    plt.imshow(image)
    plt.axis('off')
    label = "Red Cube" if prediction > 0.5 else "Green Cube"
    plt.title(f"Prediction: {label} (Confidence: {prediction:.2f})")
    plt.show()
    return 'r' if prediction > 0.5 else 'g'

letter_to_send = predict_image("photo_1_2025-07-05_16-39-17.jpg")

arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2) 
arduino.write(letter_to_send.encode())
print(f"Sent '{letter_to_send}' to Arduino.")
arduino.close()