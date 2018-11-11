def my_method(arg1,arg2):
    return arg1+arg2

my_method(2,4)


# To add unlimited number of arguments
def new_method(*args):
    return sum(args)

new_method(2,3,4,5)
# positional argument should be given first before the keyword argument

def kwargs(name,location, arg):
    print(name)
    print(location)
    print(arg)

def method(*args, **kwargs):
    print(kwargs)
    print(args)

method(1,2,3,4,4,5,name="harsh", location="sjsu")
