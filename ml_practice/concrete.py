import pandas as pd

from ucimlrepo import fetch_ucirepo 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt

concrete_compressive_strength = fetch_ucirepo(id=165)

X = concrete_compressive_strength.data.features 
y = concrete_compressive_strength.data.targets 

# Normalize X using StandardScaler's fit_transform
scaler = StandardScaler()
X_norm = pd.DataFrame(scaler.fit_transform(X), columns = X.columns)

# 80/20 split using train_test_split on X_norm
X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size = 0.2, random_state=1)

def build_linear_regressor():
    """
    Build a naive linear regressor.
    """
    model = LinearRegression()
    model.fit(X_train,y_train)
    return model

def main():
    model = build_linear_regressor()

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

if __name__ == "__main__":
    main()
