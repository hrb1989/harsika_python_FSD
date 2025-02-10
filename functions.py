# functions - repeat the snippet of code when ever called. Reuse the code
# def functionname():
#   statement/operation/expression
#   function block

# Calling Function - who calls a function
# Called Function - actual function
# Args, kwargs - parameters passed to the functions - args = positional params; kwargs = nameds/keywords params and not positional | *Args - limited or known params; **args - unlimited or multiple params
# anonymous function - lambda - a function without a name but assigned to a variable
# map, filter, reduce - lambda - pre-defined functions to handle math operations

def my_function(): # function, called function
    print("Hi Harsika!!!")

my_function() # calling function

# args
var_5 = "Hi Harsika!!!"
def my_func1(n): # with args
    for i in range(n): # On the Box function/Built In Function - Creates a list with 5 elements starts from 0
        print(var_5)
my_func1(5) # calling function with args; 5 is a value for n in the called function


def my_func2(n, var): # with args
    for i in range(n): # On the Box function/Built In Function - Creates a list with 5 elements starts from 0
        print(var)
my_func2(5, var_5) # calling function with args - positional args 0: n=5 and 1: var = var_5

#kwargs - keyword args
def my_func3(n, var): # with args
    for i in range(n): # On the Box function/Built In Function - Creates a list with 5 elements starts from 0
        print(var)
my_func3(n=5, var=var_5) # calling function with kwargs - keyword args n=5 and var = var_5
my_func3(var=var_5, n=3) # calling function with kwargs - keyword args n=3 and var = var_5

# default args
def my_func4(n, var=var_5): # var got a default value as var_5
    for i in range(n): # On the Box function/Built In Function - Creates a list with 5 elements starts from 0
        print(var)
my_func4(n=5) # calling function with kwargs and no value for var
my_func4(n=2, var="Hey HRB!!!") # calling function with kwargs and no value for var

# emtpy function - futuristic purpose - use pass
def my_calculator():
    pass

# posistional args only - use / at last

def my_func2(n, var, /): # with args only
    for i in range(n): # On the Box function/Built In Function - Creates a list with 5 elements starts from 0
        print(var)
my_func2(5, var_5) # calling function with args - positional args 0: n=5 and 1: var = var_5
# my_func2(n=5, var=var_5) # calling function with args - positional args 0: n=5 and 1: var = var_5


#kwargs only - keyword args only - use * at the beginning
def my_func3(* ,n, var): # with kwargs only
    for i in range(n): # On the Box function/Built In Function - Creates a list with 5 elements starts from 0
        print(var)
my_func3(n=5, var=var_5) # calling function with kwargs - keyword args n=5 and var = var_5
# my_func3(5, var_5) # calling function with kwargs - keyword args n=3 and var = var_5


# mixed args - some posital and some keyword
# positional needs to be at the starting and keyword needs to be at the last
#kwargs - keyword args
def my_func3(n,/,*, var): # n is positional only and var is keyword only
    for i in range(n): # On the Box function/Built In Function - Creates a list with 5 elements starts from 0
        print(var)
my_func3(5, var=var_5) # calling function with kwargs - keyword args n=5 and var = var_5
# my_func3(n=3, var=var_5) # calling function with kwargs - keyword args n=3 and var = var_5
# my_func3(5, var_5) # calling function with kwargs - keyword args n=3 and var = var_5

# infinite args
# arbitary args - *args or *var
# arbitary kwargs - **kwargs or **var

def func_ar_args(*value):
    pass

func_ar_args(1)
func_ar_args(1,2,3)
func_ar_args(1,2)

def func_ar_kwargs(**value):
    pass

func_ar_kwargs(n1=1)
func_ar_kwargs(n1=1,n2="Hello")

'''
Task:
Try the Calculator with function
Try the Tables with function
'''
# User and Auth functions
def create_user():
    pass

def user_login():
    pass

def user_logout():
    pass

def update_user():
    pass

def delete_user():
    pass

# Anonymous Function - Lambda - Function without a Name
# lambda - small, 1 line
# lambda - can accept any number of args but executes only 1 expression/statement and it returns a value
# syntax
# lambda *args: expr

sum_1 = lambda a=3,b=4: a+b 
print(sum_1)
print(sum_1())

sum_2 = lambda a,b: a+b
print(sum_2(8,6))

num_1 = int(input("Enter the value of a: "))
num_2 = int(input("Enter the value of b: "))
print(sum_2(num_1, num_2))

# usage of lambda in a normal function will change its behaviour
def multing(num):
    return lambda a:a*num

doubler = multing(2) # Passed value for num to function multing
tripler = multing(3) # Passed value for num to function multing

print(doubler(4)) # Passed value for a in lambda
print(tripler(4)) # Passed value for a in lambda