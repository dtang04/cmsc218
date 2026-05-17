import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import confusion_matrix, precision_score, accuracy_score

np.random.seed(42)
def main():
    # Preprocessing
    df = pd.read_csv("practice_data.csv")
   
    X = df.drop(columns=["churned"])

    scale = StandardScaler()
    X = scale.fit_transform(X)

    y = df["churned"]

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    log_model = LogisticRegression()
    log_model.fit(X_train, y_train)
    y_hat = log_model.predict(X_test)

    print(confusion_matrix(y_test, y_hat))
    print("Precision: (TP / (TP + FP))", precision_score(y_test, y_hat))
    print("Accuracy: (TP / (TP + FN))", accuracy_score(y_test, y_hat))

if __name__ == "__main__":
    main()
