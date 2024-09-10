

try:
    print("a")
    raise Exception("doom")  # Raises an exception with the message "doom"
except:
    print("b")  # Executes if an exception is raised in the 'try' block
else:
    print("c")  # Executes only if no exception occurs in the 'try' block
finally:
    print("d")  # Always executes, regardless of whether an exception occurred or not


#output
#a
#b
#d