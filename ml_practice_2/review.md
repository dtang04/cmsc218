# Quiz 4 Review

## 1. Classification

### Binary Classification with Linear Regression
- Convert class labels to binary (0/1)
- Fit linear regression, then round predictions at threshold 0.5
- `Y_hat = (model.predict(X_test) > 0.5) * 1.0`

### Decision Boundaries
- The line/curve where the model predicts exactly 0.5
- Linear classifiers create straight-line boundaries
- Polynomial features create curved boundaries

### Confusion Matrix
- Measures classification performance
- False positives (predicted 1, actual 0)
- False negatives (predicted 0, actual 1)
```python
from sklearn.metrics import confusion_matrix
print(confusion_matrix(Y_test, Y_hat))
```
* Rows = Actual class, Columns = Predicted class

```
                  Predicted
                0          1
            ┌─────────┬─────────┐
Actual  0   │   TN    │   FP    │
            ├─────────┼─────────┤
        1   │   FN    │   TP    │
            └─────────┴─────────┘
```

**Metrics**:
- Accuracy = (TP + TN) / Total
- Precision = TP / (TP + FP) - accuracy within predicted labels
- Recall = TP / (TP + FN) - accuracy within true labels

### Better Classifiers
- **Logistic Regression**: `LogisticRegression()` - handles multi-class automatically
- **Support Vector Machine**: `SVC()` - finds optimal separating hyperplane by minimizes hinge loss

---

## 2. Dimensionality Reduction

### Principal Component Analysis (PCA)
- Converts correlated variables into uncorrelated principal components
- First PC has largest variance, each subsequent PC is orthogonal to all other PCs (captures direction of greatest remaining variance)
- Useful for visualizing high-dimensional data in 2D

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pca.fit(X)
Z = pca.transform(X)
```

### Key PCA Outputs
- `pca.components_`: The principal component axes (weighted averages of features)
- `pca.explained_variance_ratio_`: How much variance each PC explains

### Important: Normalize Before PCA
- Features must be on same scale for meaningful variance comparison
```python
from sklearn.preprocessing import StandardScaler
X = StandardScaler().fit_transform(X)
```

---

## 3. Clustering

### K-Means Clustering
- Partitions n observations into k clusters
- Each observation belongs to cluster with nearest mean

```python
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=5)
labels = kmeans.fit_predict(X)
```

---

## 4. Neural Networks

### Key Concepts
- Networks learn by adjusting weights to minimize error
- Training uses one pass of forward + backpropogation for each epoch
- **Must standardize data** to prevent vanishing/exploding gradients

### Standardizing Data
```python
from sklearn.preprocessing import StandardScaler

std_x = StandardScaler()
std_y = StandardScaler()
X = std_x.fit_transform(X)
Y = std_y.fit_transform(Y)
```

### Building a Model (TensorFlow/Keras)
```python
import tensorflow as tf

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.InputLayer(input_shape=(8,))) # X_i =[X1...X8]
model.add(tf.keras.layers.Dense(units=20, activation='relu')) # 1st hidden
model.add(tf.keras.layers.Dense(units=12, activation='relu')) # 2nd hidden
model.add(tf.keras.layers.Dense(units=1))  # output layer

model.compile(loss="mean_squared_error",
              metrics=[tf.keras.metrics.MeanSquaredError()])

model.fit(x=X, y=Y, batch_size=1000, epochs=20, shuffle=True)
```

### Activation Functions
- `relu`: Rectified Linear Unit - max(0, x)
- `softmax`: For multi-class classification output

### Loss Functions
- **Regression**: `mean_squared_error`
- **Classification**: `SparseCategoricalCrossentropy`

---

## 5. Convolutional Neural Networks (CNNs)

### Architecture for Image Data
1. **Conv2D**: Applies filters to detect features
2. **MaxPooling2D**: Downsamples feature maps
3. **Flatten**: Converts 2D feature maps to 1D vector
4. **Dense**: Fully connected classification layers

```python
model = tf.keras.models.Sequential()

# Convolution blocks
model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 3))) # 26 x 26 x 32 (shrinks in size due to padding='valid')
model.add(tf.keras.layers.MaxPooling2D((2, 2))) # 13 x 13 x 32
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(tf.keras.layers.MaxPooling2D((2, 2))) # 5 x 5 x 64

# Classification
model.add(tf.keras.layers.Flatten()) # 1600 x 1
model.add(tf.keras.layers.Dense(64, activation='relu')) # 64 neuron layer that is connected to all 1600 nodes
model.add(tf.keras.layers.Dense(10, activation='softmax')) # takes the 64 neurons and outputs 10 probabilities (one per class)

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])
```

* `tf.keras.layers.Conv2D(filters, filter_window, activation_func)` -> (x, y, filters)
* `tf.keras.layers.MaxPooling2D(filter)`

```
Layer                    Calculation              Output
─────────────────────────────────────────────────────────
Input                                             28 x 28 x 3
Conv2D(32, 3x3)          28 - 3 + 1 = 26          26 x 26 x 32
MaxPool(2x2)             26 / 2 = 13              13 x 13 x 32
Conv2D(64, 3x3)          13 - 3 + 1 = 11          11 x 11 x 64
MaxPool(2x2)             11 / 2 = 5 (floor)        5 x  5 x 64
Flatten                  5 * 5 * 64 = 1600        1600
```

### Image Preprocessing
- Normalize pixel values: `x_train = x_train / 255.0`
- Reshape for CNN input: `x_train.reshape(60000, 28, 28, 3)`

---

## 6. Classifier Decision Boundaries

| Classifier | Boundary Shape | Code |
|------------|----------------|------|
| Logistic Regression | Linear (straight line) | `LogisticRegression()` |
| Neural Network (MLP) | Curved/non-linear | `MLPClassifier()` |
| Decision Tree | Axis-aligned rectangles | `DecisionTreeClassifier()` |

### Visualizing with PCA
```python
# Fit classifier
clf = LogisticRegression()
clf.fit(X_train, Y_train)
Y_pred = clf.predict(X_test)

# Reduce to 2D for visualization
pca = PCA(n_components=2)
Z = pca.fit_transform(X_test)

# Plot actual vs predicted
plt.scatter(Z[Y_test, 0], Z[Y_test, 1], c='r', alpha=0.1)
plt.scatter(Z[~Y_test, 0], Z[~Y_test, 1], c='b', alpha=0.1)
```

---

## Quick Reference: sklearn Imports

```python
# Preprocessing
from sklearn.preprocessing import StandardScaler, normalize

# Dimensionality Reduction
from sklearn.decomposition import PCA

# Clustering
from sklearn.cluster import KMeans

# Classification
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier

# Model Selection
from sklearn.model_selection import train_test_split

# Metrics
from sklearn.metrics import confusion_matrix, classification_report
```
