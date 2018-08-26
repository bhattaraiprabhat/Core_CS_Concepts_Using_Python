#MAP and REDUCE are very effective ways to handle data structure. Here are
#Some examples.

#   1. I have an array of Temperature in Degree F. I want to convert them to
#   Degree C. Use map to convert the temperature unit. 

DegreeF = [-40, 0,0,20,30,40, 50, 60, 70, 80, 90, 100, 110, 120, 320]

def convert_F_to_C(T):
    '''
    Conversion formula:
    (C-0)/100-0 = (F-32)/(212-32)
    --> C= (F-32)*100/180
    --> C = (F-32)*5/9
    '''
    return round((T-32)*5/9,2) #round in two decimal places 

#Note in python 3, you need to pass the map in list to convert it to list
#Note, even though convert_F_to_C method has argument T, in map we pass the
#argument as a parameter of map method.
#Here: map(convert_F_to_C,DegreeF)==> map(function, argument of function)
DegreeC= list(map(convert_F_to_C,DegreeF))


for i in range(len(DegreeF)):
    print (DegreeF[i],"F =  ", DegreeC[i],"C")


# 2. Similar example: given I have an array x, create another array that is
# x^3-2x+2

import random
arr = [random.randint(0,10) for _ in range (10)]
print ("Original array: \n",arr)

new_arr = list(map(lambda x: x**3 -2*x +2, arr))

#Here lambda expression is short form of function
"""
def func(x):
    return x**3 -2*x +2
"""

print("Original array mapped to a function: \n",new_arr)

# 3. Find sum of all elements of an array using reduce
arr = [random.randint(-3,3) for _ in range (10)]
print ("Original array: \n",arr)

from functools import reduce #In general you need to import this library to use reduce

sum_of_all = reduce(lambda x, y :x+y, arr)
print ("sum_of_all: ", sum_of_all)

#Equivalent function for lambda expression:
def func(x,y):
    return x+y

sum_of_all_1 = reduce(func, arr)

print ("sum_of_all_1: ", sum_of_all_1)


# 4. Use reduce to find max value in an array

def myMax(x,y):
    if x>y:
        return x
    else:
        return y
maxValue  = reduce (myMax,arr)

print ("Original array: \n",arr)
print ("Max value of array: ",maxValue)
