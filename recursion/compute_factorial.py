"""
    Factorial of a user defined number is calculated

    input: n
    return: n*(n-1)*(n-2)....*1
"""


def main():
    number = input ("Enter an integer: ")

    if (int(number)>20):
        print ("Number you are entering is too large. Please consider some \
                smaller number")
    elif int(number)<0 :
        print ("Factorial of negative integer is undefined")
    else:
        print ("Factorial of ", number, " is ", factorial(int(number)))


def factorial(n):
    if ( n==0):
        result =1
    else:
        result = n*factorial(n-1)

    return result



if __name__=="__main__":
    main()
