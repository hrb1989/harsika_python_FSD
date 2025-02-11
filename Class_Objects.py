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
    def __init__(self, name, email, gender, city, dob=""): # this will be auto triggered when a object created
        self.name = name # self. is to tell the system that this is a property of particular object
        if dob:
            self.__dob = dob
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

    def show_dob(self):
        return self.__dob

# creation of new object
person_1 = Person("Harsika", "02-02-2004", "harsika@gmail.com", "Female", "Madurai")
person_2 = Person("HRB", "18-11-1989", "hrb@gmail.com", "Male", "Chennai")

print(person_1.name)
person_2.introduce()
person_1.introduce()

# Inheritance - Parent child relationship - Creation of a sub class or child class from an existing class (parent class)
# Method Overriding
# Encapsulation - Securing a property/method
    # Access specifiers - Public, Protected, Private - public, _protected, __private
    # public - can be accessed from everywhere
    # _protected - same like public but need an _
    # __private - can be accessed only with the class not not outside

# Child Class:
class Employee(Person): # Employee class got created from a parent class named Person
    # property
    def __init__(self, name, email, gender, city, degree, passout, experience, skill):
        super().__init__(name, email, gender, city) # self will not be used as we are calling the parent and sharing the values with parent
        self.degree = degree
        self.passout = passout
        self.experience = experience
        self.skill = skill

    # method
    def prof_qualification(self):
        print("I have a {} degree with {} years of experience".format(self.degree, self.experience))

emp_1 = Employee("Hiran", "hrb@mjit.in", "Male", "Bengaluru", "BE", 2011, 14, "Infrastructure Automation")

print(emp_1.city)
emp_1.introduce() # object of class Employee can access method of Person as well
emp_1.prof_qualification()

class Human():
    def __init__(self, hair, hand, leg, speak, hear):
        self.hair = hair
        self.hand = hand
        self.leg = leg
        self.speak = speak
        self.hear = hear

class Employee2(Person, Human): # Employee2 class got created from a parent classes named Person and Human
    # property
    def __init__(self, name, email, gender, city, degree, dob, passout, experience, skill, hair=True, hand=True, leg=True, speak=True, hear=True):
        Person.__init__(self, name, email, gender, city, dob) # with super() self is not required, but with a class name like Person, self required
        Human.__init__(self, hair, hand, leg, speak, hear)
        self.degree = degree
        self.passout = passout
        self.experience = experience
        self.skill = skill

    # method
    def prof_qualification(self):
        print("I have a {} degree with {} years of experience".format(self.degree, self.experience))

    # Method overriding: - same method, but different block of statement/expr on each class
    def introduce(self):
        print("Hi, My Name is {}, I can work on {}".format(self.name, self.skill))

emp2_1 = Employee2("Hiran", "hrb@mjit.in", "Male", "Bengaluru", "BE", "18/Nov/89", 2011, 14, "Infrastructure Automation")

print(emp2_1.city)
emp2_1.introduce() # object of class Employee can access method of Person as well
emp2_1.prof_qualification()

# Inheritance - 1 Parent & n childs; n parents & 1 child possible

# print(emp2_1.__dob)
print(emp2_1.show_dob())
