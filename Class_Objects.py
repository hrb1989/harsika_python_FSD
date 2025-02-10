# OOP - Object Oriented Programming
# We dont want to reinvent the wheel
# Reusage is the key
# Create a blueprint with the properties and actions for a object and create as many objectas as possible

# Person
# Property: - Definition - has, have, part of, in, with, 
# name, dob, email, gender, city
# action: What can it perform - Functions/Methods
# introduce, eating, sleeping

# harsika - object - instance of a class Person
# hiran - object - instance of a class Person

class Person: # Class name needs to always starts with a Capital Letter
    # Default initialization method
    # 1st argument in a class will always be a self
    def __init__(self, name, dob, email, gender, city): # this will be auto triggered when a object created
        self.name = name # self. is to tell the system that this is a property of particular object
        self.dob = dob
        self.email = email
        self.gender = gender
        self.city = city

    # method
    def introduce(self): # self args will call all the properties of class Person
        print("Hi, I am {} and I live in {}".format(self.name, self.city))

    # method
    def sleep():
        pass

    # method
    def eat():
        pass

# creation of new object
person_1 = Person("Harsika", "02-02-2004", "harsika@gmail.com", "Female", "Madurai")
person_2 = Person("HRB", "18-11-1989", "hrb@gmail.com", "Male", "Chennai")

print(person_1.name)
person_2.introduce()
person_1.introduce()

# Inheritance
# Method Overriding
# Encapsulation
    # Access specifiers - Public, Protected, Private