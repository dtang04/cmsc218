import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.decomposition import PCA

from sklearn.metrics import r2_score, accuracy_score, confusion_matrix, recall_score, precision_score

import tensorflow as tf

np.random.seed(42)

def main():
    df = pd.read_csv("Airline_Delay_Cause.csv").dropna()
    
    # Separate into quantitative and categorical features
    q_features = ["year", "month", "weather_ct"]
    cat_features = ["carrier", "airport"]

    X_q = df[q_features]
    X_c = df[cat_features]

    scale = StandardScaler()
    X_q = scale.fit_transform(X_q)

    encoder = OneHotEncoder(sparse_output=False)
    X_c = encoder.fit_transform(X_c)

    X = np.hstack([X_q, X_c])

    y = (df["arr_del15"] > 0).astype(int) # 0 if no delays, 1 if delay

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    # ----Logistic Regression Model----
    log_model = LogisticRegression()
    log_model.fit(X_train, y_train)
    y_hat = log_model.predict(X_test)
    print("Accuracy: ", accuracy_score(y_test, y_hat))

    # ----Neural Network----
    
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.InputLayer(input_shape=(X.shape[1],)))
    model.add(tf.keras.layers.Dense(64, activation="relu"))
    model.add(tf.keras.layers.Dense(32, activation="relu"))
    model.add(tf.keras.layers.Dense(16, activation="relu"))
    model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

    #model.compile(optimizer="adam", loss="mse", metrics=["mae"])
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

    model.fit(X_train, y_train, class_weight={0: 35, 1: 1})

    loss, acc = model.evaluate(X_test, y_test)

    y_hat = model.predict(X_test)

    y_hat = (y_hat > 0.5).astype(int).flatten() # make y_hat discrete [0,1], deal with class imbalance by labelling 1 only with very high probability (> 0.7)

    print(confusion_matrix(y_test, y_hat))
    print("Precision: ", precision_score(y_test, y_hat))
    print("Recall: ", recall_score(y_test, y_hat))

    # High Precision - Of all the delays predicted positive, >99% were indeed true positives
    # Low Recall - Of all the delays in the dataset, only ~70% were caught by our classifier

if __name__ == "__main__":
    main()