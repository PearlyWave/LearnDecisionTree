#!/usr/bin/env python
# -*- coding: utf-8 -*-
# demo.py BY Eric USING PyCharm
# AT 2019/12/22 12:08
# TOPIC :

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
if __name__ == '__main__':
    clf = RandomForestClassifier(random_state=0)
    X = [[1, 2, 3],  # 2 samples, 3 features
         [11, 12, 13]]
    y = [0, 1]  # classes of each sample
    print(clf.fit(X, y))
    print(clf.predict(X))
    print(clf.predict([[4,5,6],[14,15,16]]))


    Z = [[0, 15],
         [1, -10]]
    print(StandardScaler().fit(Z).transform(Z))
