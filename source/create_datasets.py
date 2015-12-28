"""

Walmart 2015 @ Kaggle
@author:Abhishek


"""


import pandas as pd
import numpy as np
from collections import Counter

train = pd.read_csv('../data/train.csv', dtype={'Upc': object})
test = pd.read_csv('../data/test.csv', dtype={'Upc': object})
train_visits = train.VisitNumber.values
test_visits = test.VisitNumber.values
train = train.drop('TripType', axis=1)

data = pd.concat([train, test])

def check_digit(x):
    try:
        odd = map(int, ','.join(x[-1::-2]).split(','))
        even = map(int, ','.join(x[-2::-2]).split(','))
        sum_odd3 = sum(odd) * 3
        total = sum_odd3 + sum(even)
        rem = total % 10
        if rem == 0:
            return rem
        return 10 - rem
    except:
        return -9999

data['check'] = data.Upc.apply(check_digit)

def full_upc(x):
    try:
        if len(x) < 12:
            missing = 11 - len(x)
            zeros = ['0'] * missing
            xx = zeros + ','.join(x).split(',') + [str(check_digit(x))]
            xx = ''.join(xx)
            return xx
    except:
        return -9999

data['full_upc'] = data.Upc.apply(full_upc)

data = data.drop('Upc', axis=1)

def company(x):
    try:
        p = x[:6]
        if p == '000000':
            return x[-5]
        return p
    except:
        return -9999

data['company'] = data.full_upc.apply(company)

data.to_csv('../data/fulldata.csv', index=False)


from sklearn import preprocessing
data = data.fillna(-9999)
for col in data.columns:
    print col
    if col not in [u'VisitNumber', u'ScanCount']:
        lbl = preprocessing.LabelEncoder()
        data[col] = lbl.fit_transform(data[col].values)


data.to_csv('../data/full_data_enc.csv', index=False)
