"""
    This is a classical mathematical problem. There are n discs named 1, 2, 3,
    ....with hole at center which are stacked in decreasing order. There are three pillars numbered A B and C. 
    All the discs are placed in pillar A in the beginning. And the objective is to transfer the
    discs in pillar 3 keeping the decreasing size order intact

    Best practice for this problem is to create an array of source,
    destination and intermediate steps and append the value in them
    accordingly. 

"""

def main():
    print_header()
    num_of_discs= int(input("Enter number of discs: "))

    tower_of_henoi(num_of_discs, "A", "C", "B")


def print_header():
    print()
    print("######################################################")
    print("########### Tower of Henoi                 ###########")
    print("######################################################")
    print()
   
def tower_of_henoi(n, SOURCE, DESTINATION, INTERMEDIATE):
    if n==1:
        print("Move disc ",n, " from ", SOURCE, " to ", DESTINATION)
        return
    tower_of_henoi(n-1, SOURCE, INTERMEDIATE, DESTINATION)
    print("Move disc ", n,  " from ", SOURCE, " to ", DESTINATION)
    tower_of_henoi(n-1, INTERMEDIATE, DESTINATION, SOURCE) 

    




if __name__=="__main__":
    main()
