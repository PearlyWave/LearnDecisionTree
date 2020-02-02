#!/usr/bin/env python
# -*- coding: utf-8 -*-
# DTsPipelineOnStudent.py BY Eric USING PyCharm
# AT 2019/12/23 16:56
# TOPIC :

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd


if __name__ == '__main__':


    # create a pipeline object
    pipe = make_pipeline(
        StandardScaler(),
        LogisticRegression(random_state=0)
    )

    # load the iris dataset and split it into train and test sets
    # X, y = load_iris(return_X_y=True)
    df = pd.read_csv(r'student_en.csv')
    mylist = df.values.tolist()
    X = []
    y = []
    for i in mylist:
        y.append(i.pop())
        X.append(i)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    # fit the whole pipeline
    pipe.fit(X_train, y_train)


    # we can now use it like any other estimator
    print("%.2f" % accuracy_score(pipe.predict(X_test), y_test))