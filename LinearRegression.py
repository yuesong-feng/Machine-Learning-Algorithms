import numpy as np


class LinearRegression:
    def __init__(self):
        self.coef_ = 0
        self.intercept_ = 0
        self.n_iter_ = 100
        self.learning_rate = 0.01

    def fit(self, X, y):
        for i in range(self.n_iter_):
            self.coef_ -= self.learning_rate * self.derivation_coef_(X, y)
            self.intercept_ -= self.learning_rate * self.derivation_intercept_(X, y)
        return

    def derivation_coef_(self, X, y):
        derivation_coef_ = 0
        for i in range(len(X)):
            derivation_coef_ += 2 * (y[i] -(X[i] * self.coef_ + self.intercept_)) * (-X[i])
        return derivation_coef_

    def derivation_intercept_(self, X, y):
        derivation_intercept_ = 0
        for i in range(len(X)):
            derivation_intercept_ += 2 * (y[i] - (X[i] * self.coef_ + self.intercept_)) * (-1)
        return derivation_intercept_

    def loss(self, X, y):
        loss = 0
        for i in range(len(X)):
            loss += (y[i] - (X[i] * self.coef_ + self.intercept_)) ** 2
        return loss

    def predict(self, X):
        y_test = X * self.coef_ + self.intercept_
        return y_test


if __name__ == '__main__':
    X_train = np.array([0, 1, 2, 3, 4])
    y_train = np.array([1.3, 2.2, 3.6, 4.2, 5.7])
    X_test = np.array([2, 3, 4])
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    print(lr.coef_, lr.intercept_)
    print(lr.loss(X_train, y_train))
    print(lr.predict(X_test))
