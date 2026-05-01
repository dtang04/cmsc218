import numpy as np
import pandas as pd

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import TimeSeriesSplit
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor

from sklearn.metrics import r2_score

def main():
    df = pd.read_csv("student_performance.csv")
    df["prev_exam_score"] = df.groupby("student_id")["exam_score"].shift(1)

    df = df.dropna(how="any")

    encoder = OneHotEncoder(sparse_output=False)
    tutor = encoder.fit_transform(df[["tutoring"]])

    features = ["student_id", "hours_studied", "sleep_hours", "attendance_pct", "prev_exam_score"]
    X = df[features]

    scalar = StandardScaler()
    norm_X = scalar.fit_transform(X)
    norm_X = pd.DataFrame(np.hstack([norm_X, tutor]))

    y = df[["exam_score"]]

    scaler_y = StandardScaler()
    norm_y = scaler_y.fit_transform(y).reshape(-1,1).ravel()

    tscv = TimeSeriesSplit(n_splits=5)
    for train_idx, test_idx in tscv.split(X):
        # Standard OLS
        X_train, y_train = norm_X.iloc[train_idx], norm_y[train_idx]
        X_test, y_test = norm_X.iloc[test_idx], norm_y[test_idx]

        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        r_2OLS = r2_score(y_test, y_pred)
        print(f"R^2 of OLS: {r_2OLS}")

        # MLP
        model = MLPRegressor()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        r_2MLP = r2_score(y_test, y_pred)
        print(f"R^2 of MLP: {r_2MLP}")
        print("___________")

if __name__ == "__main__":
    main()