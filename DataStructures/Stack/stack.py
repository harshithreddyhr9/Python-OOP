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

    def push(self,value):
        self.stackList.append(value)
        
    def pop(self):
      if self.isEmpty():
        return None
      return self.stackList.pop()
          
stack = myStack()
for i in range(5):
    stack.push(i)
print ("isEmpty(): " + str(stack.isEmpty()))
print ("top() " + str(stack.top()))
print ("size() " + str(stack.size()))