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
If we need to print the variables of the employee then it will be a troublesome to call each variable. 
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


