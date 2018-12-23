class myStack:  
    def __init__(self):
        self.stackList = []

    def isEmpty(self):
      return self.size() == 0

    def top(self):
      if self.isEmpty():
        return None
      return self.stackList[-1] # return last element of the list
    
    def size(self):
      return len(self.stackList)
          
stack = myStack()
print ("isEmpty(): " + str(stack.isEmpty()))
print ("top() " + str(stack.top()))
print ("size() " + str(stack.size()))