#!/usr/bin/env python
# -*- coding: utf-8 -*-
# DecisionTreeOnStudent1.py BY Eric USING PyCharm
# AT 2019/12/23 16:45
# TOPIC :

from sklearn.ensemble import RandomForestClassifier
import pandas as pd
if __name__ == '__main__':
    clf = RandomForestClassifier(random_state=0)
    df = pd.read_csv(r'student_en.csv')
    mylist = df.values.tolist()
    X = []
    y = []
    for i in mylist:
        y.append(i.pop())
        X.append(i)
    clf.fit(X, y)
    print(clf.predict([[1,0,0,3,0,0,0,2]]))