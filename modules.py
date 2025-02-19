# import functions # Call another python file with its name
# import built_in_functions
# import json
# import os
import datetime
# import sys
# import math
# import random
# import asyncio
# import pandas
# import numpy
# import Class_Objects
# from Class_Objects import Employee # Import only specific class or function
# from Class_Objects import * # Not Recommended

# functions.my_func1()

# print(built_in_functions.var_1)

print(datetime.datetime.today().day)
# print(Class_Objects.emp2_1.name)

# Emp_1 = Employee("HRB","hrb@mjit.in","Male","Chennai","BE",2011,14,"Infra Automation")

# To make a list of files under a folder to be available as a module, we need to create a __init__.py file in the folder
# modules needs to be listed in bashrc or env variables
import os

file = open("README.md")
content = file.read()
print(content)
file.close()


file = open("test.txt", 'w')
file.write("Hello Harsika")
file.close()

file = open("test.txt")
content = file.read()
print(content)
file.close()

os.chdir("H:\\")
print(os.getcwd())