import pandas as pd
from sklearn.model_selection import TimeSeriesSplit
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score

def main():
    df = pd.DataFrame({
        "value": [10, 12, 13, 15, 18, 21, 19, 23, 25, 28, 30, 29, 60, 58, 39, 29, 18, 38, 48, 29, 384, 82, 28, 128, 348, 4, 28, 38, 48, 281, 28, 348, 21, 38, 29, 28]
    })

    df["value_prev"] = df.shift(1)
    df.dropna(inplace=True)
    tscv = TimeSeriesSplit(n_splits=2)

    X = df[["value_prev"]]
    X = StandardScaler().fit_transform(X)

    y = df[["value"]]
    y = StandardScaler().fit_transform(y)

    count = 1
    for train_idx, test_idx in tscv.split(X):
        print(f"Train idx [fold={count}]", train_idx)
        print(f"Test idx [fold={count}]", test_idx)

        X_train, y_train = X[train_idx], y[train_idx]
        X_test, y_test = X[test_idx], y[test_idx]
    
        log_model = LinearRegression()
        log_model.fit(X_train, y_train)

        y_pred = log_model.predict(X_test)

        print("R^2 score: ", r2_score(y_test, y_pred))

        count += 1

if __name__ == "__main__":
    main()