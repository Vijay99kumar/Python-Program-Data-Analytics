# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 20:34:38 2021

@author: Rajneesh Sharma
"""

print("hello world")
#numbers
#a=3  b=5 #a and b are number objects

#string
str1 = 'hello students' #string str1
str2 = ' how are you' #string str2
str1
str2
print(str1 + str2) #printing the concatention of str and str2
print (str1[0:5]) #printing first five character using slice operator 
(str1[0:5])
print (str1[4]) #printing 5th character of the string 
print (str1*2) #printing the stirnf twice

#LIst
l = [1, "hi" ,"python", True]
print (l[3:])
print (l[0:2])
print (l)
print (l + l)
print (l * 3)
print (type(l))
#lets try mutation 
l[1] = "bye"
print (l)

#tuple
t = ('hi' , 'python' , 2, 4)
t
print (t[1:]); 
print (t[0:3]);
print (t);
print (t + t)
print (t * 3)
print (type(t))
#lets try to mutation 
t[1] ="bye" 
print (t)

#dictionary
d = {1:"jimmy" , 2:'alex' , 3:'john' , 4:'mike'}
d
print("1st name is "+d[1])
print("2st name is "+d [4])
print (d);
print (d.keys());
print (d.values());

#-------ADVANCED------
#List
#ordered collection of item; sequence of items in list
shoplist =['apple' , 'carrot', 'mango' , 'banana']
shoplist
len(shoplist)
print(shoplist)

#add item to lst
shoplist.append('rice')
shoplist

#short
shoplist.sort() #inplace sort 
shoplist
 
#index/select
shoplist[0]
shoplist[0:4]

#delete item
del shoplist[0]
shoplist

#tuple
#used  to hold multiple object similar to lists; less fucntionality than list 
#immutable - cannot modify - fast; ()
zoo = ('python' , 'lion' , 'elephant' , 'bird' )
zoo
len(zoo)
language = 'c' , 'java' , 'php' , 1  #better to put () , this also worka
language 
type(language)

#Dictionary - like an addressbook use of associate keys with values
#key-value pairs {'key1' : 'value1', 'key2': 'value2'} {} bracket , : colon 
student = {'A101':'ANUBHAV' , 'A102':'RAVI' , 'A103':'PRAFULL' , 'A104': 'KARAN'}
student
student['A103']
print('name of roll no A103 is ' + student['A103'])
del student['A104']
student
len(student)

#for  rollno , name in student.item ():
    #print('name of {} is {} '.format(rollno, name)) 

#lets test mutation
#adding a value
student['A104'] = 'HITESH'
student

#set
Anubhav = {1,2,3,4,5}
Anubhav
Aman_1 = set()
Aman_1

#sets are unordered collection  of objects; ([ , ])
teamA = set(['india' , 'enland' , 'australia' , 'bangladesh' , 'ireland'])
teamA
teamB = set(['pakistan' , 'south africa' , 'bangladesh' , 'ireland'])
teamB

#Checking whether a data value exists in a set or not.
'india' in teamA
'india' in teamB

#adding value in a set
teamA.add('china')
teamA #put in order
teamA.add('india')
teamA #no duplicates
teamA.remove('australia')
teamA

#Create dataframe :
import pandas as pd

#Create a dataframe 
d = {'Name':['Alisa','Bobby','Cathrine','Alisa','Bobby','Cathrine',
             'Alisa','Bobby','Cathrine','Alisa','Bobby','Cathrine'],
             'Exam':['Semester 1','Semester 1','Semester 1','Semester 1','Semester 1','Semester 1',
                    'semester 2','semester 2','semester 2','semester 2','semester 2','semester 2'],
                     'Subject':['Mathematics','Mathematics','Mathematics','Science','Science','Science',
                               'Mathematics','Mathematics','Mathematics','Science','Science','Science'],
                                 'Score':[62,47,55,74,31,77,85,63,42,67,89,51]}
d

df = pd.DataFrame(d,columns=['Nmae','Exam','Subject','Score'])

df

     
 




























