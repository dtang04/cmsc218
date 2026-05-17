import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.decomposition import PCA

from sklearn.metrics import confusion_matrix, precision_score, accuracy_score

import tensorflow as tf

np.random.seed(42)

def main():
    # ----Logistic Regresion----

    # Preprocessing
    df = pd.read_csv("practice_data.csv")
   
    X = df.drop(columns=["churned"])

    scale = StandardScaler()
    X = scale.fit_transform(X)

    y = df["churned"]

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    log_model = LogisticRegression()
    log_model.fit(X_train, y_train)
    y_hat = log_model.predict(X_test)

    print(confusion_matrix(y_test, y_hat))
    print("Precision: (TP / (TP + FP))", precision_score(y_test, y_hat))
    print("Accuracy: (TP / (TP + FN))", accuracy_score(y_test, y_hat))

    # ----PCA----
    pca = PCA(n_components=2)
    pca.fit(X) # fit PCA basis
    Z = pca.transform(X) # project X onto PCA basis

    churned = y == 1
    plt.scatter(Z[churned, 0], Z[churned, 1], c='r', alpha=0.5, label='Churned')
    plt.scatter(Z[~churned, 0], Z[~churned, 1], c='b', alpha=0.5, label='Stayed')
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.legend()
    plt.title('PCA: Churned vs Stayed')
    plt.show(block=False)

    # ----Neural Network----
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.InputLayer(input_shape=(X.shape[1],)))
    model.add(tf.keras.layers.Dense(64, activation='relu')) # relu for hidden layers prevent vanishing gradients
    model.add(tf.keras.layers.Dense(32, activation='relu'))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid')) #logistic regression (binary classification)

    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

    model.fit(X_train, y_train, epochs=50) # 50 forward + backprop cycles

    loss, acc = model.evaluate(X_test, y_test)

    print(loss, acc)

if __name__ == "__main__":
    main()
