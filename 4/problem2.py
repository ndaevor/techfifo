try:
    # The 'try' block is executed first. Here, it prints "a".
    print ("a")
except:
    # The 'except' block would execute if an exception was raised in the 'try' block.
    # Since no exception occurs here, this block is skipped.
    print ("b")
else:
    # The 'else' block executes only if no exception occurred in the 'try' block.
    # Because no exception was raised, this block executes and prints "c".
    print ("c")
finally:
    # The 'finally' block always executes, regardless of whether an exception occurred or not.
    # It executes after the 'try', 'except', and 'else' blocks (if the 'else' block executed).
    # This block prints "d".
    print ("d")


#output
#a
#c
#d