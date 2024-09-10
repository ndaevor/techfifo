#number of multiplications

numcalls = 0
def square(x):
    global numcalls
    numcalls = numcalls + 1
    return x * x

print(square(5))  #one multiplication inside the function (x=5)

print(square(2*5)) #one multiplication before calling function (2*5) and one multiplication inside function (x=10)