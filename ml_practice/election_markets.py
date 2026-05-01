"""
Building a model to predict number of candidate votes.
"""

import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge

from sklearn.neural_network import MLPRegressor

from sklearn.model_selection import train_test_split

from sklearn.metrics import r2_score

df = pd.read_csv("1976-2020-president.csv")
df = df.fillna(0)

def main():
    features = ["year", "state", "party_simplified", "office"]
    encode = OneHotEncoder(sparse_output=False)
    X = encode.fit_transform(df[features])

    y = df["candidatevotes"]

    # Need to standardize y for MLP because y-labels aree large -> exploding gradients
    scaler = StandardScaler()
    y = scaler.fit_transform(pd.DataFrame(y)).reshape(-1,1).ravel() # Get to 1-D array using ravel

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print(f"R^2 Score of OLS Model: ", r2_score(y_test, y_pred))

    model = Ridge(alpha=5)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"R^2 Score of Ridge Model: ", r2_score(y_test, y_pred))

    model = MLPRegressor() # default: 1 hidden layer, 100 neurons, relu activation func
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"R^2 Score of MLP Model: ", r2_score(y_test, y_pred))


if __name__ == "__main__":
    main()
