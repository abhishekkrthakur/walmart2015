"""

Walmart 2015 @ Kaggle
@author:Abhishek


"""

import pandas as pd
import numpy as np


data = pd.read_csv('../data/fulldata.csv')
data = data.drop_duplicates('VisitNumber')
visit = np.unique(data.VisitNumber.values)

WEEKDAY = {'Sunday': 1,
           'Monday': 2,
           'Tuesday': 3,
           'Wednesday': 4,
           'Thursday': 5,
           'Friday': 6,
           'Saturday': 7
           }


with open('../full_weekday.libsvm', 'w') as f:
    for k, v in enumerate(visit):
        trip = data[data['VisitNumber'] == v]
        w = trip.Weekday.values[0]
        f.write('{}\n'.format(' '.join([str(-1)] + [str(WEEKDAY[w]) + ':' + str(1)])))
        if k % 1000 == 0:
            print k