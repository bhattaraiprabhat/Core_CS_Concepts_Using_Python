#In this program we briefly introduce "list" and implement it in simple cases


import random
#At first we create a random array. You can turn on "seed" by un-commenting
#line with seed operation to make constant array. Changing argument of seed
#creates new list. 

#------------------------------------------------------------------------
#random.seed(0)
#------------------------------------------------------------------------

#There are multiple ways to create array. un-comment one that you like the
#most for your use case

#------------------------------------------------------------------------
#Using append method
myList = []
for _ in range(12):
    randomInt = int(10*random.random())%10
    myList.append(randomInt)
#------------------------------------------------------------------------

#------------------------------------------------------------------------
#Using list comprehension
#myList = [random.randint(1, 12) for _ in range(10)]
#------------------------------------------------------------------------
print ("My Original list:  \n", myList)


#------------------------------------------------------------------------

#Find length of an array (total number of elements in the array:
arrayLength = len(myList)
print ("Size of myList " , arrayLength)
#------------------------------------------------------------------------

#Iterate through array elements: 
#There are multiple ways to iterate through elements.

#------------------------------------------------------------------------
for i in myList:
    print (i , end =' ')
    #end = ' ' works in python 3 only
print ()

#------------------------------------------------------------------------

for i in range(len(myList)):
    print (myList[i], end = ' ')
print()
#------------------------------------------------------------------------

print (list(i for i in  myList))

#------------------------------------------------------------------------
#In this way we can keep track of position id and value together
for count, i in enumerate(myList):
    print (count , i)

#Similar way:
for i in range(len(myList)):
    print (i, myList[i])

#------------------------------------------------------------------------
#reversed method changes prints the array in reversed order
for i in reversed(range(len(myList))):
    print (myList[i] , end =' ')
print ()
#------------------------------------------------------------------------


#------------------------------------------------------------------------
#Sorting an array:
print ("Sorted Array:")

sortedList = sorted(myList) #Ascending order 
print (sortedList)
revSortedList = list(reversed(sorted(myList))) #Descending order
print (revSortedList)
#------------------------------------------------------------------------


#------------------------------------------------------------------------
#Find min & max

minVal = min(myList)
maxVal = max(myList)

print ("Minimum of myList : ",minVal, "\nMaximum of myList: ", maxVal)
#------------------------------------------------------------------------

#------------------------------------------------------------------------
#Swap elements of array
#In this example last element and first element of array are swapped
print ("Array before swapping:")
print (myList)
print ("Array array swapping:")
myList[0], myList[len(myList)-1] = myList[len(myList)-1],myList[0]
print (myList) #Check the place values of first and list element




