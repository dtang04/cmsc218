"""
Practice 2: CNN with MNIST

Topics:
- Conv2D, MaxPooling2D, Flatten, Dense
- Multi-class classification (10 classes)
- softmax + sparse_categorical_crossentropy
- Confusion matrix for multi-class
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from sklearn.metrics import confusion_matrix


def main():
    mnist = tf.keras.datasets.mnist
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    X_train = X_train / 255
    X_test =  X_test / 255

    X_train = X_train.reshape(len(X_train), 28, 28, 1) # reshape to include channel
    X_test = X_test.reshape(len(X_test), 28, 28, 1)

    # Architecture:
    #   Conv2D(32, (3,3), relu, padding='same') -> 28x28x32
    #   MaxPooling2D((2,2)) -> 14x14x32
    #   Conv2D(64, (3,3), relu, padding='same') -> 14x14x64 - deeper layers trade off dimensionality reduction with more filters
    #   MaxPooling2D((2,2)) -> 7x7x64
    #   Flatten -> 3136
    #   Dense(64, relu)
    #   Dense(10, softmax) <- 10 digit classes

    # CNN
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Conv2D(32, (3,3), activation='relu', padding='same'))
    model.add(tf.keras.layers.MaxPooling2D((2,2)))
    model.add(tf.keras.layers.Conv2D(64, (3,3), activation='relu', padding='same'))
    model.add(tf.keras.layers.MaxPooling2D((2,2)))
    model.add(tf.keras.layers.Flatten())

    # Classification NN
    model.add(tf.keras.layers.Dense(64, activation='relu'))
    model.add(tf.keras.layers.Dense(10, activation='softmax'))

    model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(), metrics=['accuracy'])
    
    model.fit(X_train, y_train, epochs=5, batch_size=64)


    # Evaluate on test set
    loss, acc = model.evaluate(X_test, y_test)

    # Get predictions and print confusion matrix
    y_pred = np.argmax(model.predict(X_test), axis=1) # max probability is the highest predictor
    print(confusion_matrix(y_test, y_pred))
    print(loss, acc)
    


if __name__ == "__main__":
    main()
