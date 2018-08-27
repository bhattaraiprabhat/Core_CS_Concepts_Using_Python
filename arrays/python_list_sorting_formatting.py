#In this example python standard sorting and some other basic formatting
#issues are discussed.


#/////////////////////////////////////////////////////////////////
# sorted and sort()    
#/////////////////////////////////////////////////////////////////

#Consider a list

list1 = ["a", "z", "p", "b", "k", "a"]

#sorted

list2 = sorted(list1)

#This is list1
print ("This is list1");
print (list1)
print ("This is list2");
print (list2)

#Sort changes the list permanently
list1.sort()

#This is list1
print ("This is list1. Note sort() changes the list permanently");
print (list1)
print ("This is list2");
print (list2)


#/////////////////////////////////////////////////////////////////
# sort by key    
#/////////////////////////////////////////////////////////////////
list3 = ["aaaa", "z", "ppp", "bbbb", "kkk", "aaaaa"]

list4= sorted(list3,key=len)

list5= sorted(list3,key=len,reverse=True)

print ("This is list3");
print (list3)
print ("This is list4.  Note: The list has been sorted by key=len of array element");
print (list4)
print ("This is list5.  Note: The list has been sorted by key=len and in reverse order");
print (list5)



#/////////////////////////////////////////////////////////////////
# sort using any element in array   
#/////////////////////////////////////////////////////////////////


def sorting_func(string):
    return string[-2]# second last element

list6 = ["apple", "ball", "cat", "dog", "elephant", "fish"]

list7 = sorted(list6, key=sorting_func)

print ("This is list6");
print (list6)
print ("This is list7.  Note: Ordered by second last element. See sorting_func");
print (list7)



#/////////////////////////////////////////////////////////////////
# List Comprehension  
#/////////////////////////////////////////////////////////////////

#A compact way of manipulate an array in loop

list8 = [0,1,2,3,4,5]

list9 = [i*i for i in list8]

print ("This is list8");
print (list8)
print ("This is list8.  Note: List comprehension is used to find square of  elements");
print (list9)


list10 = ["apple","ball","cat","dog"]

list11 = ["@"+i.upper() for i in list10]
list12 = ["@"+i.upper() for i in list10 if i[0].upper()<'C']

print ("This is list10");
print (list10)
print ("This is list11.  Note: List comprehension is used to change entries to upper case and add other");
print (list11)


print ("This is list12.  Note: List comprehension is used to change entries to upper case with conditionals");
print (list12)





