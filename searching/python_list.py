#In this program we briefly introduce searching implementation in list


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

#------------------------------------------------------------------------
# Find a random element within the range of list and search if the element is
# found in the myList

newrandomInt = int(10*random.random())%10

print ("newrandomInt ",newrandomInt)

#Python search:
if newrandomInt in myList:
    print (newrandomInt, " is present in the myList")
else:
    print (newrandomInt, " is missing the myList")



#Linear Search:

for i in range(len(myList)):
    if myList[i]==newrandomInt:
        print (newrandomInt, " is present in the myList in position  ", i)
    else:
         (newrandomInt, " is missing the myList")


#Binary search:
#1. It requires sorted array to act on
#2. Following binarySearch() function is recursive method
myList= sorted(myList)
print (myList)

def binarySearch(myList, searchItem, firstID,lastID):
    if firstID<=lastID:
        midID = (firstID+lastID)//2
        print ("firstID ", firstID, " lastID ", lastID, " midID ", midID, " searchItem ", searchItem )

        if myList[midID]==searchItem:
            print (searchItem, " is found at location ", midID)
            return (searchItem, midID)
        elif  searchItem>myList[midID]:
            return binarySearch(myList, searchItem, midID+1,lastID)
        elif  searchItem<myList[midID]:
            return binarySearch(myList, searchItem, firstID,midID-1)
    else:
        print (searchItem, " not found")
binarySearch(myList, newrandomInt,0, len(myList)-1)


def binarySearchNonRecursive(myList,searchItem):
    first = 0
    last = len(myList)
    while first<=last:
        mid=(first+last)//2
        if searchItem>myList[mid]:
            first =mid+1
        elif searchItem<myList[mid]:
            last = mid-1
        else:
            print (searchItem , " found at location ", mid)
            return


print ("Method 2")
binarySearchNonRecursive(myList,newrandomInt)
