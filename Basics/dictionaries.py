my_set = {1,3,5}
#dict = {'key':value}
my_dict = {'name': 'Harshith', 'age':23, 'dob': "09/20/1995"}

another_dict = {1:10,2:20,3:30}

# a dictionary cannot perform any operations
Student_details = { # Dictionary 
    'name' : 'Harshith',
    'subjects': (202,272,273)
}



universities = [ # List of dictionaries
    {
        'name': 'SJSU',
        'location': 'San Jose'
    },
    {
        'name': 'MVSR',
        'location': 'India'
    }
]

print(universities[0]) # prints the first dictionary
print(Student_details['name']) # With dictionary you can access a value with a key


################################
# A class is a blueprint

class student:
    def __init__(self,name): # A object will get the properties defined in __init__()
        self.name = name
        self.subjects = (202,272,273)

    def total(self):
        return sum(self.subjects)

s = student("Harshith") # Object created
print(s.name) 
print(s.subjects)
print(s.total())


