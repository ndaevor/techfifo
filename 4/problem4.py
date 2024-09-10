def f():
    try:
        print("a")
        return  # This return statement exits the function
    except:
        print("b")  # This block is skipped because no exception occurs
    else:
        print("c")  # This block is skipped because the 'try' block contains a return statement
    finally:
        print("d")  # This block always executes, regardless of what happens before it

f()


#output
#a
#d