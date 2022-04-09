# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 11:09:04 2022

@author: Vijay Kumar
"""
#-----------------------MISSING Values---------------------------

#Counting the missing values---------------
import pandas as pd
import numpy as np

# create a Dataframe

df1 = {'subject':['semester1','semester2','semester3','semester4','semester1','semester2',
                  'semester3'],
       'score':[62,47,np.nan,74,np.nan,77,85]}

df1 = pd.DataFrame(df1,columns=['subject','score'])
print(df1)

'''Is there any missing Values in dataframe'''
df1.isnull()
df1.notnull()

'''Is there any missing Values across columns'''
df1.isnull().any()

'''Is there any missing Values across each columns'''
df1.isnull().sum()

#Dropping rows with Missing Values-----------------

#Create Dataframe

df_1 = {'Name':['sanjay','vishal','shiv kumar','Nitin kumar','Dev yadav','Shivam',np.nan],
        'State':['UP','RJ','MP','UT','punjab','Goa',np.nan],
        'Gender':['M','F','M','F',np.nan,np.nan,np.nan],
        'score':[68,54,78,np.nan,75,np.nan,np.nan]} 
df_1 = pd.DataFrame(df_1,columns=['Name','State','Gender','score'])
    
print(df_1)

#Drop all rows that have any NaN(Missing) Vilues
df_1.dropna()

#Drop only if a row has NaN Vilues
df_1.dropna(how='all')   

#Drop all rows that have any NaN(Missing) Vilues
df_1.dropna(thresh=2)





