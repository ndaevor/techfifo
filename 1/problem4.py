#output of the problem

x = 1
def f():
    x = 2
    return x
print(x)
print(f())
print(x)

""""
output
1
2
1

print(x) prints value inside variable x 
print(f()) calls the function f which returns a value which is also also x but locally declared inside the function (x=2)
prints(x) again prints value of x which is declared globally

"""


