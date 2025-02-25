import numpy as np
from Perceptron import Perceptron
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import datasets

def accuracy(y_true, y_pred):
    return np.sum(y_true == y_pred) / len(y_true)

X, y = datasets.make_blobs(n_samples=1500, n_features=2, centers=2, cluster_std=1.05, random_state=12)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

p = Perceptron()
p.fit(X_train, y_train)
pred = p.predict(X_test)

print('accuracy: ', accuracy(y_test, pred))
print('weights: ', p.weights)
print('bias: ', p.bias)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.scatter(X_train[:, 0], X_train[:, 1], marker="o", c=y_train)

x0_1 = np.amin(X_train[:, 0])
x0_2 = np.amax(X_train[:, 0])

x1_1 = (-p.weights[0] * x0_1 - p.bias) / p.weights[1]
x1_2 = (-p.weights[0] * x0_2 - p.bias) / p.weights[1]

ax.plot([x0_1, x0_2], [x1_1, x1_2], "k")

ymin = np.amin(X_train[:, 1])
ymax = np.amax(X_train[:, 1])
ax.set_ylim([ymin - 3, ymax + 3])

plt.show()