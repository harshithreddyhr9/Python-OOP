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
    def go_to_school(self):
        return self.name + " is going to " +self.school
    
    @staticmethod
    def schools(): # Doesnt take any objects because it is a static method.
        return "I am going to school"
    
    @classmethod
    def schoolname(cls):
        print("The school name is" +cls.school)

Harshith = Student("Harshith", "SJSU")
Harshith.marks.append(93) # The list has been appended
Harshith.marks.append(89)
print(Harshith.average()) 
print(Harshith.go_to_school())
print(Harshith.schools())

Messi = Student("Messi", "Barcelona")
print(Messi.go_to_school())
Harshith.schoolname() # if it is a class method, an object can call the method or a class
Student.schoolname()

