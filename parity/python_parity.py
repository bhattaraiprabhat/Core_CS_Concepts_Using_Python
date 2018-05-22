"""
    Parity in a binary word accounts for the number of ones (set bits). 

    Even number of set bits  --> 0 parity
    Odd  number of set bits  --> 1 parity

"""
def main():
    """
    Following code prints the parity of numbers starting from 1 and extending
    to 10
    """
    for i in range (1, 10):
        #print ("Basic method......\n")
        #print (i, bin(i)[2:].zfill(8), " parity: ", parity_basic(i))
        #print ("Slight improvement over basic method......\n")
        print (i, bin(i)[2:].zfill(8), " parity: ", parity(i))



#This function has small improvement over parity_basic
def parity (x):
    parity_result =0

    while (x):
        parity_result ^= x & 1
        x >>= 1
        
    return parity_result


def parity_basic(x):
    """ 
        count the number of set bits and then find modulo to decide if it has
        even or odd number of ones
    """

    count_set_bits=0
    while (x):
        count_set_bits+=x&1
        x>>=1
    if count_set_bits%2==0:
        print ("Even parity...........")
    else:
        print ("Odd parity ...........")
    return count_set_bits%2
    
if __name__=="__main__":
    main()
