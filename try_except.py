# TRY and EXCEPT
# try and except statements are used to handle errors in Python.


# example 1
try:
    print(x)
except:
    print("An exception occurred")
else:
    print("No exception occurred")
finally:
    print("The 'try except' is finished")


# example 2
try:
    print("I will try to divide 10 by 2")
    print(10/2)
    print("I will try to divide 10 by 0")
    print(10/0)
except ZeroDivisionError:
    print("You can't divide by 0")
except:
    print("An error occurred")
else:
    print("No exceptions occurred")
finally:
    print("The 'try except' is finished")