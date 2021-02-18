#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ashwin Srinivasan
"""
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import metrics 



dataset = pd.read_csv('data1.csv')


#plot1 - count number of fraud values
dataset['isFraud'].value_counts().plot(kind='bar')
dataset['isFraud'].value_counts()

#plot2 - time variable and most transactions occur in the first half of our sample
dataset['step'].hist()

#Plot 3 - type of transaction
dataset['type'].value_counts().plot(kind='bar')

plt.scatter(dataset['oldbalanceOrg'], dataset['amount'], alpha=0.5)
plt.show()

dataset['merchant'] = dataset['nameDest'].str.contains('M')

features = ['step',
            'type',
            'amount',
            'oldbalanceOrg',
            'newbalanceOrig',
            'oldbalanceDest',
            'newbalanceDest',
            'merchant']

label = ['isFraud']

x = dataset[features]
y = dataset[label]

x = x.join(pd.get_dummies(x[['type']], prefix='type')).drop(['type'], axis=1)

from sklearn.model_selection import train_test_split 

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)


from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

model.fit(X_train, y_train)
preds = model.predict(X_test)
print(model.score(X_test,y_test))
ac = accuracy_score(y_test,preds)
print('Accuracy is: ',ac)

from sklearn.tree import DecisionTreeClassifier 

clf = DecisionTreeClassifier()

clf = clf.fit(X_train,y_train)

y_pred = clf.predict(X_test)

print(clf.score(X_test,y_test))
ac = accuracy_score(y_test,y_pred)
print('Accuracy is: ',ac)

metrics.plot_confusion_matrix(clf, X_test, y_test)