import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

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

def main():
    # Naive Linear Regressor
    model = buildLinearRegressor(X_train, y_train)
    print("Naive Linear Regression R^2: ", model.score(X_test, y_test))

    # Check if there is any correlation visually between month number and sunspots
    plt.scatter(df["Month_No"], df["Sunspots"])
    plt.show()

    model = buildLinearRegressor(X_train_n, y_train)
    print("AR(1) Model R^2: ", model.score(X_test_n, y_test_n))


if __name__ == "__main__":
    main()

