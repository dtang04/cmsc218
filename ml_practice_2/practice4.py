import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.decomposition import PCA

from sklearn.metrics import r2_score, accuracy_score

import tensorflow as tf

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
    model.add(tf.keras.layers.Dense(32)) # regression, no activation func
    model.add(tf.keras.layers.Dense(16))
    model.add(tf.keras.layers.Dense(1))

    model.compile(optimizer="adam", loss="mse", metrics=["mae"])

    model.fit(X_train, y_train)

    loss = model.evaluate(X_test, y_test)

    y_pred = model.predict(X_test)

    print("R^2: ", r2_score(y_test, y_pred))
    print("Loss: ", loss)

if __name__ == "__main__":
    main()