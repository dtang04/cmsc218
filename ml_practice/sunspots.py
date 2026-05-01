import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.model_selection import TimeSeriesSplit

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge

df = pd.read_csv("monthly-sunspots.csv")

df["Month_No"] = df["Month"].apply(lambda x: int(x.split('-')[1]))

df["prev_Sunspot"] = df["Sunspots"].shift(1) # Shift all Sunspots down one column (lag-1)
df = df.dropna(how = "any")

X = df[["Month_No"]] # Have to use dataframes for training set, not series

y = df["Sunspots"]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

X_new = df[["Month_No", "prev_Sunspot"]]
X_train_n, X_test_n, y_train_n, y_test_n = train_test_split(X_new, y, random_state=1)

def buildLinearRegressor(X_, y_):
    model = LinearRegression()
    model.fit(X_, y_)
    return model

def buildRidgeRegressor(X_, y_, l = 5):
    model = Ridge(alpha=l)
    model.fit(X_, y_)
    return model

def main():
    # Naive Linear Regressor
    model = buildLinearRegressor(X_train, y_train)
    print("Naive Linear Regression R^2: ", model.score(X_test, y_test))

    # Check if there is any correlation visually between month number and sunspots
    plt.scatter(df["Month_No"], df["Sunspots"])
    plt.show()

    # Should not use train_test_split on AR(1) models, as it does not respect time order (data leakage)
    # model = buildLinearRegressor(X_train_n, y_train)
    # print("AR(1) Model R^2: ", model.score(X_test_n, y_test_n))

    model_tscv = None
    fold = 1
    tscv = TimeSeriesSplit(n_splits=5) # trains on past data and tests on future data, five-fold split
    for train_idx, test_idx in tscv.split(X):
        X_train_fold, X_test_fold = X_new.iloc[train_idx], X_new.iloc[test_idx]
        y_train_fold, y_test_fold = y.iloc[train_idx], y.iloc[test_idx]

        model_tscv = buildLinearRegressor(X_train_fold, y_train_fold)
        model_ridge_tscv = buildRidgeRegressor(X_train_fold, y_train_fold)

        r2 = model_tscv.score(X_test_fold, y_test_fold)
        r2_ridge = model_ridge_tscv.score(X_test_fold, y_test_fold)

        y_pred = model_tscv.predict(X_test_fold)
        y_pred_ridge = model_ridge_tscv.predict(X_test_fold)
    
        r = np.corrcoef(y_test_fold, y_pred)[0,1] #Returns [0,1]th element of correlation matrix
        r_ridge = np.corrcoef(y_test_fold, y_pred_ridge)[0,1]

        print(f"AR(1) Model OLS: fold = {fold}, R = {r}, R^2 = {r2}")
        print(f"AR(1) Model Ridge: fold = {fold}, R = {r_ridge}, R^2 = {r2_ridge}")

        fold += 1
    
    # New data
    X_new_pts = pd.DataFrame({"Month_No": [5, 3, 2], "prev_Sunspot": [100, 30, 75]})
    print(model_tscv.predict(X_new_pts))
    
if __name__ == "__main__":
    main()

