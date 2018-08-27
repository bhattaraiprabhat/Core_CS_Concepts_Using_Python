#In this program we work on some basic problems on indices of array and
#operations like sum, difference etc.


import random

def main():
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
    indices_for_specific_sum(myList,5)



def indices_for_specific_sum(arr,val):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            mySum= arr[i] +arr[j]
            if mySum ==val:
                print ("Array in indices ", i ," and ", j," sum up to ", mySum) 
                









if __name__=="__main__":
    main();

