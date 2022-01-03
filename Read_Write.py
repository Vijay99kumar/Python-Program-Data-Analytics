# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 20:21:24 2022

@author: Rajneesh Sharma
"""

#-------------------------Reading & Writing data in Files----------------------

import pandas

# Reading CSV Files with Pandas:
df = pandas.read_csv('D:/PyData/New Data/User_Data.csv')
print(df)

# Writing CSV Files with Pandas:
df.to_csv('D:/PyData/New Data/IIT-B.csv')

# Reading Excel Files with Pandas
df1 = pandas.read_excel('D:/PyData/New Data/User_Data1.xlsx')

#df1 = pandas.read_excel('User_Data.xlsx')
print(df1)

# Writing Excel Files with Pandas 
df1.to_excel('D:/PyData/New Data/IIT-B.xlsx')
df2 = pandas.DataFrame(df1)
print (df2)
