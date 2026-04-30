"""
Topics Covered:

Linear Regression:
LinearRegressor(), fit

Ridge Regression:
Ridge(alpha), fit

R^2:
model.score(X,y)

Normalization:
scale = StandardScaler()
X_norm = scale.fit_transform(X)

Polynomial Matrix:
scale = PolynomialFeatures(deg)
X_poly = scale.fit_transform(X)

Train-test-split:
X_train, X_test, y_train, y_test = train_test_split(X, y)
"""


import pandas as pd

from ucimlrepo import fetch_ucirepo 

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge

import matplotlib.pyplot as plt

concrete_compressive_strength = fetch_ucirepo(id=165)

X = concrete_compressive_strength.data.features 
y = concrete_compressive_strength.data.targets 

# Normalize X using StandardScaler's fit_transform
scaler = StandardScaler()
X_norm = pd.DataFrame(scaler.fit_transform(X), columns = X.columns)

# 80/20 split using train_test_split on X_norm
X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size = 0.2, random_state=1)

def build_linear_regressor(X_, y_):
    """
    Build a naive linear regressor.
    """
    model = LinearRegression()
    model.fit(X_, y_)
    return model

def build_ridge(X_, y_, reg = 0):
    model = Ridge(alpha = reg)
    model.fit(X_,y_)
    return model

def main():
    model = build_linear_regressor(X, y)

    # R^2 score of naive linear regressor
    print("R^2 score of linear regressor: ", model.score(X_test, y_test))
    
    #  Determine coefficients
    colnames = X_norm.columns
    coefs = model.coef_
    print("__________________")
    print("Model Coefficients")
    for i, col in enumerate(colnames):
        print(col + ": ", coefs[0][i])
    print("________________")

    plt.scatter(X_norm["Superplasticizer"], y)
    plt.show()

    # There is a large hotspot at around x = -1 that may be decreasing the accuracy of the model.
    X_norm_adj = X_norm[X_norm["Superplasticizer"] > -1]
    y_adj = y[X_norm["Superplasticizer"] > -1]
    
    X_adj_train, X_adj_test, y_adj_train, y_adj_test = train_test_split(X_norm_adj, y_adj, random_state=1)

    adj_model = LinearRegression()
    adj_model.fit(X_adj_train, y_adj_train)
    print("R^2 score of adjusted linear regressor: ", adj_model.score(X_adj_test, y_adj_test))

    plt.scatter(X_norm_adj["Superplasticizer"], y_adj)
    plt.show()

    ridge_model = build_ridge(X_adj_train, y_adj_train, 5)
    print("R^2 score of ridge regressior: ", ridge_model.score(X_adj_test, y_adj_test))

    # Polynomial feature space
    poly = PolynomialFeatures(degree=3)
    X_poly = poly.fit_transform(X_norm_adj)

    X_poly_train, X_poly_test, y_poly_train, y_poly_test = train_test_split(X_poly, y_adj, random_state=1)

    # Build ridge regression model using X_poly
    poly_ridge_model = build_ridge(X_poly_train, y_poly_train, 5)
    print("R^2 score of ridge regressor trained on poly feature space: ", poly_ridge_model.score(X_poly_test, y_poly_test))

if __name__ == "__main__":
    main()
