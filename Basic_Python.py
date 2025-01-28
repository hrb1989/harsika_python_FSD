# Comment - Singel line comment
'''
multi line text
or
multi line comment
'''
"""
multi line text
or
multi line comment
"""
# in python - no difference between single or double quotes
# comments will be skipped by interpretor while executing

# Output Statement:
# print() - syntax

print("") # Empty Print/output statement

# to print numbers - no quotes
# to print anything else - '' or ""

print(55)
print("Hello World!")
print('Hello World!')

# Python is case sensitive
# Print("Hello World!")
# Python is indentation based, so use it carefully
# print("Hello") # Space from any statement is called indentation
# Python is a scripting Language, it uses interpretor and not compilor
# Python executes from Left to Right & Top to Bottom
# Python do not need line terminators like ;
# Python is a dynamic language, we do not need to specify the data type
# Variable is what holds the values


var_1 = 10 # automatically idetifies as number/integer
var_2 = 22.87 # automatically idetifies as number/float
var_3 = "HRB"
var_4 = (1,2,3,4)
var_5 = [1,2,3,4]
var_6 = False
var_7 = {1,2,3,4}
var_8 = {
    'name':"Hiran Ram Babu",
    'company': "Maho Jase IT",
    'mobile': 8825410600,
    'emailID': "info@mjit.in"
}

var_1 = 44.25
var_2 = "Harsika"

# Datatype:
# Integer
# Float
# String
# Tuple
# List
# Boolean
# Set
# Dictionary

# Python has lot of built in functions: some are as follows
# print() - output
# type() - returns data type
# range()
# input() - gets input from user
# str() - converts to string
# int() - converts to int
# float() - converts to float
# list() - converts to list
# tuple()
# set()
# dict()
# bool()

print(type(var_1))
print(type(var_2))
print(type(var_3))
print(type(var_4))
print(type(var_5))
print(type(var_6))
print(type(var_7))
print(type(var_8))

# input statement
# input() - syntax

name = input()
print("Entered name is:", name)

# input() by default stores as str()

mobile = input("Enter your mobile number: ") # with help text
print(type(mobile))

# Type casting - converting 1 datatype to another datetype
mobile = int(input("Enter your mobile number: ")) # converts the user input to int
print(type(mobile))