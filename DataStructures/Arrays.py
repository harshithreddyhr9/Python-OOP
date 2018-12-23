import array

'''type: 'd' (decimal), initializer list: [1, 2, 3]'''
newArray = array.array('d', [1, 2, 3])
print(newArray[0]) # output 1.0

'''----------Array slicing-------------------------------'''
InitializerList = [2, 5, 43, 5, 10, 52, 29, 5]
NumberArray = array.array('i', InitializerList)

print(NumberArray[1:5]) # 2nd to 5th
print(NumberArray[:-5]) # beginning to 4th
print(NumberArray[5:])  # 6th to end
print(NumberArray[:])   # beginning to end

''' output
array('i', [5, 43, 5, 10])
array('i', [2, 5, 43])
array('i', [52, 29, 5])
array('i', [2, 5, 43, 5, 10, 52, 29, 5])
'''


'''
Changing or adding array elements
----------------------------------------------------------------

Arrays are mutable; their elements can be changed in the same way as list elements. 
'''

integers = array.array('i', [1, 2, 3, 5, 7, 10])

# changing first element
integers[0] = 0    
print(integers) # array('i', [0, 2, 3, 5, 7, 10])

# changing 3rd to 5th element
integers[2:5] = array.array('i', [4, 6, 8])   
print(integers)     # Output: array('i', [0, 2, 4, 6, 8, 10])


'''Just as with lists, we can add one item to an array using the append() method or add several items using the extend() method.
'''
numbers = array.array('i', [1, 2, 3])

numbers.append(4)
print(numbers)  # array('i', [1, 2, 3, 4])

# extend() appends iterable to the end of the array
numbers.extend([5, 6, 7]) 
print(numbers)     # array('i', [1, 2, 3, 4, 5, 6, 7])


# Concatenating 2 arrays 
odd = array.array('i', [1, 3, 5])
even = array.array('i', [2, 4, 6])

integers = array.array('i')   # creating empty array of integer
integers = odd + even

print(integers) 

'''--------------------------------------------------- Deletion of array elements------------------------------
To delete one or more items from an array, use the del statement as with lists.'''

integerArray = array.array('i', [1, 2, 3, 3, 4])

del integerArray[2] # removing third element
print(integerArray) # Output: array('i', [1, 2, 3, 4])

del integerArray # deleting entire array
print(integerArray) # Error: array is not defined


'''We can use the remove(val) method to remove the given item or the pop(val) method to remove an item at the given index.
The remove() method removes the first element that equal to val in the list.'''

IntegerArray = array.array('i', [10, 11, 12, 12, 13])

IntegerArray.remove(12)

print(IntegerArray)   # array('i', [10, 11, 12, 13])

print(IntegerArray.pop(2))   # Output: 12

print(IntegerArray)   # array('i', [10,11,13])





