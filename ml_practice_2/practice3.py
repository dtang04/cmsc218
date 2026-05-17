"""
Practice 3: CNN from scratch with Fashion MNIST

Dataset: 28x28 grayscale images of clothing
10 classes: T-shirt, Trouser, Pullover, Dress, Coat,
            Sandal, Shirt, Sneaker, Bag, Ankle boot
"""

import numpy as np
import tensorflow as tf


from sklearn.metrics import confusion_matrix

def main():
    # Load Fashion MNIST
    fashion = tf.keras.datasets.fashion_mnist
    (X_train, y_train), (X_test, y_test) = fashion.load_data()

    X_train = X_train / 255
    X_test = X_test / 255

    X_train = X_train.reshape(len(X_train), 28, 28, 1)
    X_test = X_test.reshape(len(X_test), 28, 28, 1)

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Conv2D(64, (3,3), activation="relu", padding="same"))
    model.add(tf.keras.layers.MaxPooling2D((2,2)))
    model.add(tf.keras.layers.Conv2D(128, (3,3), activation="relu", padding="same"))
    model.add(tf.keras.layers.MaxPooling2D((2,2)))
    model.add(tf.keras.layers.Conv2D(256, (3,3), activation="relu", padding="same"))
    model.add(tf.keras.layers.MaxPooling2D((2,2)))
    model.add(tf.keras.layers.Flatten())

    model.add(tf.keras.layers.Dense(64, activation="relu"))
    model.add(tf.keras.layers.Dense(10, activation="softmax"))

    model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(), metrics=['accuracy'])

    model.fit(X_train, y_train, epochs=5, batch_size=64)

    loss, acc = model.evaluate(X_test, y_test)

    y_pred = np.argmax(model.predict(X_test), axis=1)
    print(confusion_matrix(y_test, y_pred))
    print(loss, acc)

if __name__ == "__main__":
    main()
