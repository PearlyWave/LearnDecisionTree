#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ImportExcelFile.py BY Eric USING PyCharm
# AT 2019/12/23 15:37
# TOPIC : Try to import a excel file

import pandas as pd

df = pd.read_csv (r'student_en.csv') #for an earlier version of Excel, you may need to use the file extension of 'xls'
print (df)
mylist = df.values.tolist()
X = []
y = []
for i in mylist:
    y.append(i.pop())
    X.append(i)
print(X)
print(y)

