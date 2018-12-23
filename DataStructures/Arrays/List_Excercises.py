'''
1. Removing even integers from the list
'''

list = [1,2,3,4,5,6,7,8,9,10]

def removeEven(list):
    return [i for i in list if i%2!= 0]

'''
2. Merge two lists. A merged list sorted list consisting of all elements of both input lists.
'''

def mergeArrays(lst1,lst2):
    i = 0
    j = 0
    while(i<len(lst1) and j<len(lst2)):
        if(lst1(i) > lst2(j)):
            lst1.insert(i, lst2(j))
            i +=1
            j +=1
        else :
            i +=1
    if j < len(lst2):
        lst1.extend(lst2[j:])
    return lst1

'''
3. Find two numbers in the list that add up to a number
'''

