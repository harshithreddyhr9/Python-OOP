# Python-OOP

1. Creating classes

``` 
class Employee:
  pass 
```
If you want to leave a class without defining anything, write pass inside it. 

2. Creating instances of a class
```
emp1 = Employee()
emp2 = Employee()
```
If you print the two objects, you can see that they are two different objects with different locations.

```
print(emp1)
print(emp2)
```

```
output: <__main__.Employee object at 0x051EA050>
<__main__.Employee object at 0x051EA070>
```

Instance variable contain data which are unique. 

3. Creating an init method inside the class.

```
class Employee:
  def __init__(self):
```
This is like a constructor. By convention *self* is passed. But you can name it whatever you want. Whenever the object is created the __init__ method will be called. 


Employee example

```
class Employee:
  def __init__(self, first, last, email):
      self.first = first
      self.last = last
      self.email = first + '.' + last + '@company.com'

emp1 = Employee('Harshith', 'Reddy')
print(emp1.first)
print(emp1.last)
print(emp1.email)
```

```
output: 
Harshith
Reddy
Harshith.Reddy@company.com
```
If we need to print each attribte of the employee then it will be a troublesome. 
So we can define another method called fullname()

```
def fullname(self):
    return '{} {}'.format(self.first, self.last)
```
When we call the method with the instance variable
```
print(emp_1.fullname())
```
emp_1 is passed as an argument to the fullname(). 

Another way of doing this is by using classname

```
print(Employee.fullname(emp_1))
```
we pass emp_1 instance because the fullname() does not know which instance to take. In place of self, emp_1 is passed and emp_1.first and emp_1.last are printed.

# Class variables

Class variables can be accessed inside a method using the class name or class instance. Class variables should be same. 
* Instance varaibles are inside the init method using self. 

```
class Employee:
    raise.amount = 1.04
    def __init__(self, first, last, pay): # you can name it anything but it conventially put self"""     self.first = first
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} , {} Email: {}'.format(self.first, self.last, self.email)
    
    def applyraise(self):
        self.pay = int(self.pay * self.raise_amount)

  
emp_1 = Employee('Harshith' , 'Reddy', 500)
emp_2 = Employee('Lionel' , 'Messi', 10)
print(emp_1.raise_amount)    
```
We can see that the raise amount is 1.04

```
output: 1.04
```

If we check the namespace of emp_1 instance.
```
print(emp_1.__dict__)
```

```
output: 
{'first': 'Harshith', 'last': 'Reddy', 'pay': 500, 'email': 'Harshith.Reddy@company.com'}
```
Now let's check Employee namespace

```
print(Employee.__dict__)
```

```
output: 
{'__module__': '__main__', 'num_of_emps': 2, **'raise_amount': 1.04,** '__init__': <function Employee.__init__ at 0x0563E228>, 'fullname': <function Employee.fullname at 0x0563E300>, 'applyraise': <function Employee.applyraise at 0x0563E348>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}
```
raise_amount is a class variable. 
Using self.raise_amount in the applyraise() method can help assigning different values of raise_amount to different instances of the class. 
```
emp_1.raise_amount = 2.5
print(emp_1.__dict__)
```
The namespace of emp_1 looks like
```
output:
{'first': 'Harshith', 'last': 'Reddy', 'pay': 520, 'email': 'Harshith.Reddy@company.com', 'raise_amount': 1.05
```
raise_amount has been added to its namespace. In this way we can assign different raise amount values to different instances without changing the original value of the class varaible. 
