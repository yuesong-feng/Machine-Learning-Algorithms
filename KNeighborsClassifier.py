import numpy as np
import collections

class KNeighborsClassifier:
    def __init__(self):
        self.n_neighbors = 5
        self.points = []

    def fit(self, X, y):
        # 保存所有点的信息
        for i in range(len(X)):
            self.points.append([X[i], y[i]])
        return

    def predict(self, X):
        classification = []
        # 计算要预测的点到数据集中每一个点的距离
        for i in range(len(X)):
            distance = []
            for j in range(len(self.points)):
                distance.append(sum((X[i] - self.points[j][0]) ** 2))
            # distance是当前点到数据集中每一个点的距离
            tmp = self.points
            for k in range(len(tmp)):
                tmp[k].append(distance[k])
            tmp = sorted(tmp, key=lambda x:x[2])
            # tmp是一个有三项的数组，第一项是numpy数据点，第二项是类别，第三项是距离，按照距离从小到大排序
            # 接下来计算距离最近前n个点的概率最大的类别
            neighbors = []
            for i in range(self.n_neighbors):
                neighbors.append(tmp[i][1])
            neighbors = collections.Counter(neighbors)
            classification.append(neighbors.most_common(1)[0][0])
        return classification

if __name__ == "__main__":
    X_train = np.array([[1, 1], [2, 2], [1, 1.5], [3, 2], [3, 4.5], [3.2, 4.3]])
    y_train = np.array([0, 0, 0, 1, 1, 1])
    knn = KNeighborsClassifier()
    knn.fit(X_train, y_train)
    X_test = np.array([[1.5, 1.3], [2, 1.8], [4, 5]])
    y_predict = knn.predict(X_test)
    print(knn.points)