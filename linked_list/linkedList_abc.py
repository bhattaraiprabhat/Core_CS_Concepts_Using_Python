"""
    As the title of the file suggests, this file contains some of first
    principles of linkedList in python. 
    There is small syntactic difference between linkedList in python compared
    to other languages such as C++, Java etc. 

    Because it is introduction and for pedagogical purpose, this program may
    contain some imperfections. However, it servers great in understanding the
    concept and it works fine. 
"""

import random


def main():
    ll =LinkedList()

    #Insert random values
    for i in range (10):
        data = random.randint(-10,20)
        ll.insert(data)
    print () 
    #Display values inserted in linked list
    ll.display()
    print ()
    print ("Size of the linked list ", ll.size()) 
    print ()

    #Search for a value  say 5
    print ("linked list has the value ", 5, " in following location ", ll.search(5), "\n")
    print () 


    #Delete data from the linked list

    ll.delete(5)
    print () 
    print ("Size of the linked list ",ll.size()) 
    print () 

    #Display after delete
    ll.display()

    print () 



#Define Node class
class Node(object):
    """
        This class contains two values: a data  and a pointer (called
        next_node_ptr). The data is the content of a Node  class where as the
        pointer is the address of next Node. We chain these nodes with the
        help of the pointer and create a linked list of data values. 
    """
    #Constructor
    def __init__(self, data= None, next_node_ptr = None):
        self.data= data
        self.next_node_ptr= next_node_ptr

   #Setters
    def set_data(self, new_data):
        self.data= new_data

    def set_next_ptr(self, new_next_node_ptr):
        self.next_node_ptr= new_next_node_ptr

    #Getters
        
    def get_data(self):
        return self.data

    def get_next_ptr(self):
        return self.next_node_ptr

"""
    After creating the Node class we want to 
    1. Insert values in the node
    2. Search values in the node
    3. Find Size of the list
    4. Delete contents of the node 

    To initiate it we need to define head of the List

"""

class LinkedList(object):
    """
        Defining head node
    """
    def __init__ (self, head= None):
        self.head= head

    
    def insert(self, data):
        """
            In this method we create a new node, pass a data in the node and
            then point its pointer towards previous head. 
            Afterwards, this newly created new node is new head
        """
        #Create instance of Node class
        #Insert a data in Node and name it new_node_ptr.
        #this new_node_ptr is anywhere
        new_node_ptr= Node(data)
        #Node class allows me to set two values: a data and a pointer 
        #In this new_node_ptr (instance of Node class), set pointer value to previous head. 
        new_node_ptr.set_next_ptr(self.head)
        #After doing this new_node_ptr will be new head. Previous head moves ahead
        #Then assign the head value to new_node_ptr
        self.head = new_node_ptr

    def display(self):
        """
        Displays the data in linked list
        """
        current_node_ptr = self.head

        while (current_node_ptr):
            print (current_node_ptr.get_data(), end= " --> ")
            current_node_ptr= current_node_ptr.get_next_ptr()
        print ("None")   


    

    def search(self, data):
        """
            This method searches for the location of the data in the
            linkedList

        """

        #Current pointer is set to head
        current_node_ptr = self.head
        #Initialize a boolean
        data_found =False
        #Iterate until the value is found
        while (current_node_ptr == None)  and (data_found == False):
            if current_node_ptr.get_data()==data:
                found =True
            else:
                current_node_ptr = current_node_ptr.get_next_ptr()
        if current_node_ptr is None:
            raise ValueError("data is not found in the linked list")

        return current_node_ptr

    def size(self):
        """
        This method calculates the size of the linked list, that is it counts
        number of nodes having values
        """
        #Initialize current pointer to head
        current_node_ptr = self.head
        node_counter= 0
        while current_node_ptr !=None:
            node_counter +=1
            current_node_ptr= current_node_ptr.get_next_ptr()

        return node_counter


    def delete(self, data):
        """ It delete a node having the passed data in the linked List. If
        there are multiple copies of same data in different nodes, it deletes
        the first one
        """

        #Create a current node and set it to head
        current_node_ptr = self.head

        #Create another node named previous and set it to None
        previous_node_ptr = None

        data_found = False

        while (current_node_ptr !=None) and (data_found ==False):
            if current_node_ptr.get_data()== data:
                data_found = True
            else:
                previous_node_ptr= current_node_ptr
                current_node_ptr= current_node_ptr.get_next_ptr()
        if current_node_ptr is None:
            raise ValueError("data is not present in the linked List")
        if previous_node_ptr is None:
            self.head = current_node_ptr.get_next_ptr()
        else:
            previous_node_ptr.set_next_ptr(current_node_ptr.get_next_ptr())

if __name__ =="__main__":
    main()




