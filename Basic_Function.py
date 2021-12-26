# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 09:39:04 2021

@author: Rajneesh Sharma
"""
# -*- coding: utf-8 -*-
"""

#abs(): returns the absolute value of a number.
# integer number 

integer = -20
abs(integer)
print('Absolute value of -20 is:', abs(integer))

# flooting number
flooting = -20.83
abs(flooting)
print('Absolute value of -20.83 is:', abs(flooting))

#all(): It returns true if all items passed in interable object are ture.
#Otherwise, it returns false.
#This fxn accepts an interable (such as list, dictionary,etc. ).
#all values ture

k = [1,3,4,6]
print(all(k))

# all values False

k = [0, False]
print(all(k))

# One False value 
k = [1,3,7,0]
print(all(k))

# empty iterable
k = []
print(all(k))

#--------------------------------------------------------------------------------------

#bool(): converts a value to boolen(True & False)
test1 = []
print(test1, 'is' ,bool(test1))

test1 = [0] 
print(test1, 'is' ,bool(test1))

test1 = None
print(test1, 'is' ,bool(test1))

test1 = 'easy string'
print(test1, 'is' ,bool(test1))

#sum():used to get the sum of the number of an iterable, i.e. List.
List_1 = [1,2,3,4]
s = sum(List_1)
print(s)

s = sum(List_1, 10)
print(s)

#len(): Return the length (the number of item) of an object.

strA = 'python'
print(len(strA))

#list()  create a list  in python 
# empty  list 
Gaurav = list()
print(Gaurav)

#converting string to list
string = 'abcd'
print(list(string))

#divmod(): used to get quatient and remainder  of two numbers.
#this function take two numeric argument and returns a tuple.
#both argument are required and numeric.
# Calling Function 
result = divmod(13,2)
# Displaying Result
print(result)
    
#dict(): Its constructor which create a dictionary.
# Calling function 
result = dict() # returns as empty Dictionary
print(result)

result2 = dict(a=1,b=2)
# displaying result 
print(result2)

#set(): It is used to create new set using elements passed during the call .
#It takes on iterable object as an argument and returns a  new  set object.
#callign function 
   result = set() # empty set
result2 = set('12')
result3 = set('javatpoint')
result4 = list('javatpoint')
result5 = {1,2}
print(result)
print(result2)
print(result3)
print(result4) 
print(result5)

#pow(): used to compute the power of a number .
# positive x, positive y (x**y)
print(pow(4,5))

# negative x, positive y
print(pow(-4, 4))

#tuple(): used to create a tuple object.
t1 =  tuple()
print('t1=' , t1)

# creating a tuple from a list 
l = [1,6,9]
t2 = tuple(l)
print('t2=', t2)

# creating a tuple from a string 
t1 = tuple('java')
print('t1=', t1)

#----------------------------------------------------------------------
#lambda()- Helps creating anonymous functions. 
#Lambda functions can accept any number of arguments, 
#but they can return only one value in the form of expression.

#Multiple arguments to Lambda function
x = lambda a,b:a+b 
# a and b are the arguments and a+b is the expression which gets evaluated and returned.   
print("Addition = ",x(20,10)) 

#Program to filter out the list which contains numbers  divisible by 3.
List = [1,2,3,4,10,123,22]  
Oddlist = list(filter(lambda x:(x%3 == 0),List)) 
# the list contains all the items of the list for which the lambda function evaluates to true  
print(Oddlist) 

#program to triple each number of the list using map  
List = [1,2,3,4,10,123,22] 
new_list = list(map(lambda x:x*3,List)) 
# this will return the triple of each item of the list and add it to new_list  
print(new_list)  


    






































