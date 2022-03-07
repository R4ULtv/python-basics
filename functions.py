# FUNCTIONS 

def function():  # To call a function, use the function name followed by parenthesis
    print('This is a Test')

def argument_function(name):    # Information can be passed into functions as arguments. You can add as many arguments as you want, just separate them with a comma.
    print('Hi ' + name)

def arguments_function(*args): # If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
    print(args)

def return_function():  # To let a function return a value, use the return statement
    return 'Hello World'


function()

argument_function('James')
argument_function('Robert')

arguments_function('1', '2', '3', '4')

print(return_function())