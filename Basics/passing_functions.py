def method(another):
    return another

def add_two_numbers():
    return 35+77

my_list = [1,2,3,4,5]
print(list(filter(lambda x: x!=1, my_list)))

'''
(lambda x: x * 3)(4)
means exacty

def f(x):
    return x * 3
f(4)
'''

print([x for x in my_list if x !=1]) # prefered more over filter
