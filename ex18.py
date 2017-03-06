def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r; arg2: %r"%(arg1,arg2))

def print_two_again(arg1, arg2):
    print("arg1: %r; arg2: %r" %(arg1,arg2))

def print_one(arg):
    print("arg1: %r" %arg)

def print_none():
    print("I got nothin'.")

print_two("Zed","is dead")
print_two_again("Zed", "is still dead")
print_one("Magnificent")
print_none()