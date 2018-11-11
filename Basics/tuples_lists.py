grades = [10,20,30,40]
tuple_grades = (10,20,30,40) # tuple is immutable. Cant be appended or remove an element
set_grades = {30,40,50,30} 
grades.append(40) # You can append a element at the end of the list.


def average():
    print(sum(grades)/ len(grades))

print(set_grades) # prints unordered and unique
average()
tuple_gradess = tuple_grades + (100,) # Creating a new tuple and adding 2 tuples
print(tuple_gradess) # prints (10,20,30,40,100)
print(grades[0]) # Accessing a list element with an index
set_grades.add(20) # add to the set. 
print(set_grades) 

# set operations
set_one = {1,2,3}
set_two = {2,3,4}
print(set_one.intersection(set_two)) # prints common elements
print(set_one.union(set_two)) # prints all the elements once
print(set_one.difference(set_two)) # prints what is not present in set_one
print(set_two.difference(set_one)) # prints what is not present in set_two