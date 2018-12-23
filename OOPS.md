# Python-OOP

1. Creating classes

```python 
class Employee:
  pass 
```
If you want to leave a class without defining anything, write pass inside it. 

2. Creating instances of a class
```python
emp1 = Employee()
emp2 = Employee()
```
If you print the two objects, you can see that they are two different objects with different locations.

```python
print(emp1)
print(emp2)
```

```
output: <__main__.Employee object at 0x051EA050>
<__main__.Employee object at 0x051EA070>
```

Instance variable contain data which are unique. 

3. Creating an init method inside the class.

```python
class Employee:
  def __init__(self):
```
This is like a constructor. By convention *self* is passed. But you can name it whatever you want. Whenever the object is created the __init__ method will be called. 


Employee example

```python
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

```python
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

```python
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

# Class Methods

We can define a class method by using a @classmethod (decorator). Classmethods can be used as a constructor. 

```python
@classmethod
def set_raise_amount(cls, amount):
    cls.raise_amount = amount
    
Employee.set_raise_amount(1.05)
```
Now the class variable raise_amount is changed to 1.05. 
You can use these class methods to create multiple objects. 

# Static methods

We can define a static method by using a @staticmethod (decorator). 
If you dont access any instance/ class variables then that method is a static method. 

# Subclasses

To inherit a parent class, subclass should have class Employee inside the parenthesis
```
class Developer(Employee):
  pass
```
Once an object of a subclass is created, the constructor(*__init__*) of the subclass is called. If not found then
the *__init__* method of parent class is called. 

You can check the definition of a class by using
```
print(help(Developer))
```
Method resolution order:
It is the order of execution of the *__init__* methods.
* parentclass
* subclass
* builtins.object
parent class inherits from the object class. 

If you want to use the parent class's variables. Employee has first, last, pay and Developer also has first, last, pay and not write redundant code again in the subclass init method. We can use the parent class' varaibles by using super() 
```python
class Developer(Employee):
  def __init__(self, first, last, pay, prog_lang):
      super().__init__(first,last,pay)
      self.prog_lang = prog_lang

      or
      Employee.__init__(self,first,last,pay)
      
dev_1 = Developer('Harshith', 'Reddy', 500, 'Python')
print(dev_1.email)
print(dev_1.prog_lang)
```
The developer class nows inherits the Employee class.

The entire code: 

```python
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


# subclass 
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

#subclass
class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp) # pass the instance to add to the list of employees.

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2) # passing the Developer object to add it to the list of employees.
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()
```
* isinstance() : To check if an object is an instance of a class
* issubclass() : To check if class B is a subclass of class A

```python
print(isinstance(mgr_1, Manager))
print(issubclass(Developer, Employee))
```
return Truee or False

# Special methods

Magic/Dunder init method (__init__)

```python
def __repr__(self):
    pass
    
def __str__(self):
    pass
```
These two methods are used to print the objects. 

When these two dunder methods were not defined and we printed our object 

```python
print(emp_1)

output: <__main__.Employee object at 0x052BA050>
```

If we define the __repr__ method
```python
def __repr__(self):
    return "Employee('{}','{}','{}').format(self.first, self.last, self.pay)
print(emp_1)

output: Employee('Harshith', 'Reddy', 500)
```

We can define the __str__ method as well

```python
def __str__(self):
    return '{} - {}'.format(self.fullname(), self.email)
print(emp_1)

output: Harshith Reddy - Harshith.Reddy@email.com
```

When both the methods are defined and we dont explicitly call __repr__ method then the object will be printed like defined in the __str__ method. 

The commonly used 'dunder' methods are 
* init
* repr
* str

Dunder methods let you emulate the behavior of built-in types. For example, to get the length of a string you can call len('string'). But an empty class definition doesn’t support this behavior out of the box:
```python
class NoLenSupport:
    pass

>>> obj = NoLenSupport()
>>> len(obj)
TypeError: "object of type 'NoLenSupport' has no len()"
```

To fix this, you can add a __len__ dunder method to your class:
```python
class LenSupport:
    def __len__(self):
        return 42

>>> obj = LenSupport()
>>> len(obj)
42
```
For clear understanding refer the [documentation](http://www.diveintopython3.net/special-method-names.html)

# Property decorator -Getter, Setters, and Deleters

```python
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname) # as we have added @property decorator for fullname(). While accessing it we dont need to write the parenthesis. 

```
If you want to set the fullname, we can use @fullname.setter decorator

```python
@property
def fullname(self):
    return '{} {}'.format(self.first, self.last)

@fullname.setter
def fullname(self,name):
    first, last = name.split(' ')
    self.first = first
    self.last = last
    
emp_1.fullname = 'Lionel Messi' 
# The full name will be split and stored in first and last so that the first name
and last name are also updated.
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

output:
Lionel
Lionel.Messi@email.come
Lionel Messi
```

If you want to delete the fullname, we can use @fullname.deleter decorator

```python
@fullname.deleter
def fullname(self):
    self.first = None
    self.last = None
    
del emp_1.fullname

```
