'''
-------|--------
| Data | Link  |
|------|-------|
# Node class'''


class Node:
    def __init__(self, data):
        self.data = data
        self.nextElement = None

class LinkedList:
    def __init__(self):
        self.headNode = Node(-1)


'''
----------------------------------------------------------------------------------------------------------------------------------------
The primary operations which are generally a part of the LinkedList class are listed below:

insertAtTail(data) - inserts an element at the end of the linked list
insertAtHead(data) - inserts an element at the start/head of the linked list
delete(data) - deletes an element with your specified value from the linked list
deleteAtHead() - deletes the first element of the list
search(data) - searches for an element in the linked list
isEmpty() - returns true if the linked list is empty

'''

'''------------------- Implementing isEmpty()------------------------------------------------------------------------------------------'''
class Node:
    def __init__(self, data):
        self.data = data
        self.nextElement = None

class LinkedList:
    def __init__(self):
        self.headNode = Node(-1)

    def isEmpty(self):
        if(self.headNode.nextElement == None): # Check whether the head points to None
            return True
        else:
            return False
    
list = LinkedList(); # Linked List created
print(list.isEmpty()); # Returns true

'''
Types of Insertion
The three types of insertion strategies used in singly linked-list are:

1. Insertion at the head
2. Insertion at the tail
3. Insertion at the N-th index
'''


'''
---------------1. Insertion at the head------------------------------------------------------------------------------------
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.nextElement = None

class LinkedList:
    def __init__(self):
        self.headNode = Node(-1)
    
  # Insertion at Head  
    def insertAtHead(self,dt):
        tempNode= Node(dt) # Create a new node containing your specified value 
        tempNode.nextElement = self.headNode.nextElement # The new node points to the same node as the head
        self.headNode.nextElement = tempNode # Make the head point to the new node
        return self.headNode # return the new list
  
    def isEmpty(self): 
        if(self.headNode.nextElement == None):
            return True
        else:
            return False
    
    def printList(self): 
        if(self.isEmpty()):
            print ("List is Empty")
            return False 

        temp=self.headNode.nextElement
        # Traversing the linked list     
        while(temp.nextElement!=None):
            print (temp.data , "->",
            temp=temp.nextElement)
        print (temp.data , "-> None")
        return True    

list = LinkedList()
list.printList() # prints list is empty

for i in range(1,10,1):
  list.insertAtHead(i)
list.printList()

''' ---------------2. Inserting at the tail-------------------------------------------------------------------------------'''

class Node:
    def __init__(self, data):
        self.data = data
        self.nextElement = None

class LinkedList:
    def __init__(self):
        self.headNode = Node(-1)
    
  # Insertion at Head  
    def insertAtTail(self,dt):
        tempNode= Node(dt) # Create a new node containing your specified value 
        temp = self.headNode # Begin from the head node
        while(temp.nextElement!=None): # Traverse the list
           temp = temp.nextElement 

        temp.nextElement = tempNode # Store the new node in the last node's link
        
        
        return 
  
    def isEmpty(self): 
        if(self.headNode.nextElement == None):
            return True
        else:
            return False
    
    def printList(self): 
        if(self.isEmpty()):
            print ("List is Empty")
            return False 

        temp=self.headNode.nextElement
        # Traversing the linked list     
        while(temp.nextElement!=None): # traverse the list
            print (temp.data , "->") # print the data of the node
            temp=temp.nextElement 
        print (temp.data , "-> None") # print the last node's nextelement pointing to None
        return True    

list = LinkedList()
list.insertAtTail(0)
list.insertAtTail(1)
list.insertAtTail(2)
list.insertAtTail(3)
list.printList()

'''--------------------3. Insert at Nth position---------------------------------------------------------------------------- '''

