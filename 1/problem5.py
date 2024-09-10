#output of the problem

x = 1
def f():        
        y = x
        x = 2
        return x + y
print(x)
print(f())
print(x)


"""
output
1
error: UnboundLocalError
inside the function attempting to use x before it is defined in the local scope.

corrected code:
x = 1
def f():
        global x        
        y = x
        x = 2
        return x + y
print(x)
print(f())
print(x)
1
3
2

"""