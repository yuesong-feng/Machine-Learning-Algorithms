import numpy as np

class KNeighborsClassifier:
    def __init__(self):
        self.n_neighbors = 5
        self.points = []

    def fit(self, X, y):
        for i in range(len(X)):
            self.points.append([X[i], y[i]])
        return

    def predict(self, X):
        neighbors = []
        for i in range(len(X)):
            distance = []
            for j in range(len(self.points)):
                distance.append(sum((X[i] - self.points[j][0]) ** 2))
            tmp = self.points
            for k in range(len(tmp)):
                tmp[k].append(distance[k])
            tmp = sorted(tmp, key=lambda x:x[2])
            print(tmp[0:self.n_neighbors])
        return

if __name__ == "__main__":
    X_train = np.array([[1, 1], [2, 2], [1, 1.5], [3, 2], [3, 4.5], [3.2, 4.3]])
    y_train = np.array([0, 0, 0, 1, 1, 1])
    knn = KNeighborsClassifier()
    knn.fit(X_train, y_train)
    X_test = np.array([[1.5, 1.3], [2, 1.8], [3, 3]])
    y_predict = knn.predict(X_test)
    # print(knn.points)