# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 17:18:07 2022

@author: Vijay Kumar
"""

# Simple Linear Regression

# importing  the Libraries

import pandas as pd
import matplotlib.pyplot as plt

# importing the Dataset

dataset = pd.read_csv('D:\PyData\stud_reg.csv')
print(type(dataset))

x = dataset.iloc[ :,:-1].values
y = dataset.iloc[ :, 1].values

# spliting the dataset into the Training set and Test set

 from sklearn.model_selection import train_test_split
 x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 1/3, random_state = 0)
 
 # Note: The parameter 'randam state ' is used to randomly bifurgate the dataset into training &
 # testing dataset. That number should be supplied as arguments to parameter 'randam state'
 # Which to grt maximum accuracy . And the number is decided by hit & trial nethod.

# Fitting Simple Linear Regression to the training set
 from sklearn.linear_model import LinearRegression
 regressor = LinearRegression()
 regressor.fit(x_train, y_train)
 
 # Calculating the Coefficients:
  print(regressor.coef_)
  
 # Calculating the intercepts: 
  print(regressor.intercept_)

# Predicting the Test set results
 y_pred = regressor.predict(x_test)

 # Accuracy of the MOdel
 
 # Calculating the r squared value:
 from sklearn.metrics import r2_score
 r2_score(y_test, y_pred)

#create a Dataframe
df1 = {'Actual Applicants':y_test,'Predicted Applicants':y_pred}
df1 = pd.DataFrame(df1,columns=['Actual Applicants','Predicted Applicants'])
print(df1)

# Visualising the predicted result
Line_chart1 = plt.plot(x_test, y_pred, '--' , c = 'red')
Line_chart2 = plt.plot(x_test, y_test, ':', c = 'blue')

      
  

 
 
 
 
 