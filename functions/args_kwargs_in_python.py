#We briefly describe meaning and implementation of args and kwargs in python:

def function_with_single_use_args(fruit1, fruit2, fruit3):
    print ("From function: function_with_single_use_args" )
    print ("I like ", fruit1)
    print ("I like ", fruit2)
    print ("I like ", fruit3)
    print ()
    
#We pass variables in the function as follows. 
function_with_single_use_args("apple", "orange", "grapes")

########################################################
#   Prints like
#       
#    I like  apple
#    I like  orange
#    I like  grapes 
#
########################################################


#To implement the same we can writhe the function as follows:

def function_with_multiple_use_args(*fruits):

    print ("From function: function_with_multiple_use_args" )
    for arg in fruits:
        print ("I like ", arg)
    print()
########################################################
#          Prints like:
#       
#    I like  apple
#    I like  orange
#    I like  grapes 
#
########################################################

#You can see that in  *fruits I am passing three arguments. 
#This is the meaning of args. I can use *args to pass variable number of
#arguments.
function_with_multiple_use_args("apple", "orange", "grapes")


#However, to pass key and value pair of arguments we wuse the following:
def function_with_multiple_use_kwargs(**fruits):
    print ()
    print ("From function: function_with_multiple_use_kwargs");
    for key in fruits:
        print (" Key-Value pair :: {} : {}".format(key, fruits[key]))
    print ()
function_with_multiple_use_kwargs(Apple=1, Orange="two", Mango=3)

########################################################
#          Prints like:
#       
#       Key-Value pair :: Apple : 1
#       Key-Value pair :: Orange : two
#       Key-Value pair :: Mango : 3
#
########################################################


#You can see I am passing three fruits in **fruits (**kwargs, key value arg)








