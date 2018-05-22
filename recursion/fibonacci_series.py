"""
    This module calculates Fibonacce series for a given number

    input: an integer
    return : Fibonacce series
"""

def main():
    number = input("Enter an integer : ")
    
    for i in range (int(number)):
        print ( fibonacci(i), end= ", " ) 

    print ()

def fibonacci(n):
    """
    Calculates the Fibonacci series

    input: n

    return :  1, 1, 2, 3, 5, 8, 13, ....

    """
    if n==0:
       result =0
    elif n==1:
        result =1
    else:
       result = fibonacci(n-1) + fibonacci(n-2)

    return result

if __name__=="__main__":
    main()
