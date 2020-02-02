#!/usr/bin/env python
# -*- coding: utf-8 -*-
# DecisionTree1.py BY Eric USING PyCharm
# AT 2019/12/23 14:07
# TOPIC : first program about DTs

from sklearn import tree
X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
print(clf.predict([[2.,2.],[0,0]]))
print(clf.predict_proba([[0.,0.],[0,0]]))