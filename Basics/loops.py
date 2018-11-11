my_string = "hello"

for character in my_string: # iterables are my_strings, lists, sets, tuples and more. character is an iterator my_string is an iterable
    print(character)

my_list = [1,2,3,4]

for number in my_list:
    print(number *2)

print([n for n in range(10) if n%2==0]) # prints a list of even numbers

people = ["Rolf", " john"]
people_withoutspaces = [person.strip() for person in people]
print(people_withoutspaces)

