class Student:
    school = " La Masia"
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self): # self takes in the object
        
        try:
            return sum(self.marks)/ len(self.marks)
        except:
            ArithmeticError
    @classmethod
    def friend(cls,obj, friend_name,*args):
        return cls(friend_name, obj.school,*args)


class WorkingStudent(Student): # Subclass inheriting Student class
    def __init__(self, name, school, salary): # Like a constructor
        super().__init__(name,school) # First line in a constructor will be a call to the super class __init__()
        self.salary = salary

anna = WorkingStudent("Lionel", "Barcelona", 600)
print(anna.salary)

friend = WorkingStudent.friend(anna, "Harshith", 20)
print(friend.name)
print(friend.salary)
print(friend.school)