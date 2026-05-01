import pandas as pd
import numpy as np

from sklearn.preprocessing import OneHotEncoder

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split

from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score

df = pd.read_csv("Traffic_Crashes_-_Crashes_20260430.csv", low_memory=False)

def main():
    # One-Hot encode the levels
    encoder_y = OneHotEncoder(sparse_output=False)
    y_encoded = encoder_y.fit_transform(pd.DataFrame(df["DAMAGE"]))
    features = ["POSTED_SPEED_LIMIT", "LIGHTING_CONDITION", "MOST_SEVERE_INJURY", "INJURIES_TOTAL", "INJURIES_FATAL", "INJURIES_INCAPACITATING"]

    encoder_x = OneHotEncoder(sparse_output=False)
    X_encoded = encoder_x.fit_transform(pd.DataFrame(df[features]))

    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y_encoded)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    print(f"R^2 of OLS Regressor: {r2}") # Low R^2 because DAMAGE is a categorical variable

    # Since DAMAGE is categorical, use multi-class classification (logistic regression classification)
    model = LogisticRegression()
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, df["DAMAGE"]) # Don't one-hot encode labels
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy of Logistic Regressor: {acc}")


if __name__ == "__main__":
    main()