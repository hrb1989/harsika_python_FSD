# Statements - if, if else, ladder - if elif, nested - if if else else
# statement - conditions to check if it is True or False
# statement - if true, it will execute the block, else it will go to next block

#Operators
# condition - operators - Relational operators
# > < >= <= != ==
# 1 > 2 - Greater Than ? No - False
# 1 >= 1 - Greater Than or Equals to ? Yes - True
# 1 == 1 - Equals to ? Yes - True

if (5>3):
    # block start - indentation (space at the start of the line) is there
    print("5 is bigger than 3")
print("1st Check over!!!")

# syntax
# if (condition):
#   block

if (5>6): # condition returns false
    # block start - indentation (space at the start of the line) is there
    print("5 is bigger than 6")
    # Block will execute only if the condition returns true
print("2nd check over")

if (5>6): # condition returns false
    # block start - indentation (space at the start of the line) is there
    print("5 is bigger than 6")
    # Block will execute only if the condition returns true
else:
    # when the condition fails, this else block will get executed
    print("5 is smaller than 6")
print("3rd check over")


# if else ladder
num_1 = 481
num_2 = 781
if (num_1>num_2):
    # block start - indentation (space at the start of the line) is there
    print("{} is bigger than {}".format(num_1, num_2))
    # Block will execute only if the condition returns true
elif (num_1<num_2):
    # block start - indentation (space at the start of the line) is there
    print("{} is smaller than {}".format(num_1, num_2))
    # Block will execute only if the condition returns true
elif (num_1 == num_2):
    # block start - indentation (space at the start of the line) is there
    print("{} and {} are equal".format(num_1, num_2))
    # Block will execute only if the condition returns true
else:
    # when the conditions fails, this else block will get executed
    print("Sorry Condition couldnt be met")
print("4th check over")


# nested if else
num_1 = 481
num_2 = 781
num_3 = 856
if (num_1 > num_2):
    # block start - indentation (space at the start of the line) is there
    # print("{} is bigger than {}".format(num_1, num_2))
    # Block will execute only if the condition returns true
    if (num_1 > num_3):
        print("{} is bigger than {}".format(num_1, num_3))
    elif (num_3 > num_1):
        print("{} is bigger than {}".format(num_3, num_1))
    elif (num_1 == num_3):
        print("{} and {} are equal".format(num_1, num_3))
elif (num_2 > num_1):
    # block start - indentation (space at the start of the line) is there
    # print("{} is bigger than {}".format(num_2, num_1))
    # Block will execute only if the condition returns true
    if (num_2 > num_3):
        print("{} is bigger than {}".format(num_2, num_3))
    elif (num_3 > num_2):
        print("{} is bigger than {}".format(num_3, num_2))
    elif (num_2 == num_3):
        print("{} and {} are equal".format(num_2, num_3))
elif (num_1 == num_2):
    # block start - indentation (space at the start of the line) is there
    # print("{} and {} are equal".format(num_1, num_2))
    # Block will execute only if the condition returns true
    if (num_2 == num_3):
        print("{}, {} and {} are equal".format(num_1, num_2, num_3))
elif (num_3 > num_1):
    # block start - indentation (space at the start of the line) is there
    # print("{} is bigger than {}".format(num_2, num_1))
    # Block will execute only if the condition returns true
    if (num_3 > num_2):
        print("{} is bigger than {}".format(num_3, num_2))
    elif (num_2 > num_3):
        print("{} is bigger than {}".format(num_2, num_3))
    elif (num_3 == num_2):
        print("{} and {} are equal".format(num_3, num_2))
elif (num_3 > num_2):
    # block start - indentation (space at the start of the line) is there
    # print("{} is bigger than {}".format(num_2, num_1))
    # Block will execute only if the condition returns true
    if (num_3 > num_1):
        print("{} is bigger than {}".format(num_3, num_2))
    elif (num_1 > num_3):
        print("{} is bigger than {}".format(num_1, num_3))
    elif (num_3 == num_1):
        print("{} and {} are equal".format(num_3, num_1))
else:
    # when the conditions fails, this else block will get executed
    print("Sorry Condition couldnt be met")
print("5th check over")


list_1 = (45,22,56,75)
# membership Operator - in, not in - returns true or false
print(45 in list_1) # it checks if 45 is available in list_2 items
print(22 not in list_1)


# logical operator - and, or, not
# and - both condtions needs to be true
# or - any one condition needs to be true
# not - condition must be false
# when I need to check more than 1 condition, logical operator is used

if (5 > 3 and 5 > 4):
    print("5 is greater than 3 & 4")

if (5 > 3 or 2 > 3):
    print("either 5 is bigger than 3 or 2 is greater than 3")

if (not False):
    print("It works!")

# identity operator - is, is not
var_1 = "Hiran"
var_2 = "hiran"
var_3 = "HRB"

print(var_1 is var_2)
print(var_1 is not var_3)

# Binary to Decimal
# Decimal to Binary

# 8421
# 0000 - 0
# 0001 - 1
# 0010 - 2
# 0011 - 3
# 0100 - 4
# 0101 - 5
# 0110 - 6
# 0111 - 7
# 1000 - 8
# 1001 - 9
# 1010 - 10
# 1011 - 11
# 1100 - 12
# 1101 - 13
# 1110 - 14
# 1111 - 15

# bitwise operator - &, |, ^, ~, <<, >>
# AND &
a = 7 # 111
b = 4 # 100
#a&b = 100 # 4
print(a&b)

# OR |
a = 7 # 111
b = 4 # 100
#a|b = 111 # 7
print(a|b)

# XOR ^
a = 7 # 111
b = 4 # 100
#a^b = 011 # 3
print(a^b)

# NOT ~
a = 7 # 0111
#~a = 1000 # -8
print(~a)

# right shift >>
a = 10 # 1010
# a >> 1 # 0101 = 5
print(a >> 1)

# left shift <<
b = 3 # 0011
# b << 1 # 0110 = 6
print(b << 1)

'''
simple scripts:
1. collect 3 input from user
2. 1 input for calculator operation (+, -, *, /, %)
3. 2 inputs to capture the numbers
4. validate if the value has number
5. Calculator app
'''

'''
enter the value of a: 5
enter the value of b: 15
enter the operation (+ - * / %): +
addition of a and b is 20

enter the value of a: 50
enter the value of b: 15
enter the operation (+ - * / %): -
subtraction of a and b is 35
'''

# Loops - Perform same operations, several times

var_4 = "Hi Harsika!!"
# Print this n number of times - Ex., n=5
# print(var_4)
# print(var_4)
# print(var_4)
# print(var_4)
# print(var_4)

# Definite Elements and indefinite elements - Target times known and Target times unknown
# Elements - Iterables - List, Tuple, Set, Dictionary
# Target - value number of repetation - n = 5; len(list/set/tuple/dictionary)
# for loop and while loop
# for loop - when we have iterable/elements involved in the repeatation - index based loop
# while loop - number of repetation involved in the looping system - condition based loop - high probability for infinite loops - Think about failure scenario before we use while

# for temp in iterables:
#   statement/operation/expression

# while (Condition):
#   statement/operation/expression
#   increment/decrement

n=5
# while (n>0):
#     print(var_4)
#     n=n-1

# i=0
# while i < n:
#     print(var_4)
#     i=i+1

for i in range(n): # On the Box function/Built In Function - Creates a list with 5 elements starts from 0
    print(var_4)


var_5 = "Hi Harsika"
# n = 5
# # Hi Harsika 1
# # Hi Harsika 2

# i=1
# while i <= n:
#     print(var_5, i)
#     i=i+1

for i in range(n):
    print(var_5, i+1)

# i=0
# while i < n:
#     i=i+1
#     if i == 3:
#         continue
#     else:
#         print(var_5, i)

# i=1
# while i <= n:
#     if i == 3:
#         i=i+1
#         continue
#     else:
#         print(var_5, i)
#         i=i+1

for i in range(n):
    if i+1 == 3:
        continue
    else:
        print(var_5, i+1)

n = int(input("Enter number of times to repeat: "))
i = 1
while(True):
    if i > n:
        break
    else:
        print(var_5, i)
        i=i+1

'''
Task:
Create a script:
get input range of elements start num and end num
get input of table
print only the divisible numbers in that range
Ex.,start - 51 end - 100 table - 5
55 60 65 70 75 80 85 90 95 100
Ex.,start - 51 end - 100 table - 10
60 70 80 90 100
'''