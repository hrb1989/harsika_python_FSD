# integer
var_1 = 20
print(var_1.is_integer()) # Returns True, if Integer or False

# Float
var_2 = 22.5
print(var_2.is_integer()) # Returns True, if Integer or False, if Float

# String - Variable will not change
var_3 = "hiran ram babu"
print(var_3.capitalize())
print(var_3.lower())
print(var_3.upper())
print(var_3.count('a'))
# print(var_3.join([' ','is my Name'])) # hiran ram babu is my name
print(var_3.replace(' ','_')) # hiran_ram_babu hrb@123$ ---> user@password hrb@hrb\@123$
print(var_3.split()) # ['hiran','ram','babu']
print(var_3)

# iterables - loop through - index, mutable, sequence
# tuple - index, immutable, sequence - ()
# list - index, mutable, sequence - []
# set - non-index, mutable, non-sequence, no duplicates - {} # to removes duplicates

var_4 = (15,78,57,15,22,15,35,95,74) # tuple
var_5 = [15,78,57,15,22,15,35,95,74] # list
var_6 = {15,78,57,15,22,15,35,95,74} # set

print(var_4)
print(var_5)
print(var_6)

# tuple
print(var_4.count(15)) # 3
print(var_4.index(57)) # 0 1 '2'

#set - Directly makes changes to the set - Permanent
var_6.add(76) # add an element to the set
print(var_6)
var_6.pop() # remove the first element from the set
print(var_6)
var_6.remove(78) # remove a specific element from the set
print(var_6)
var_6.clear() # clear the set
print(var_6)

# list
var_5.append(78) # adds as a last element
print(var_5)
var_5.insert(2,98) # adds element at a specific index
print(var_5.index(98)) # finds the index of the specific element
print(var_5.count(15)) # returns the number of times an element is available
var_5.pop() # removes the first element
print(var_5)
var_5.remove(98) # removes the specific element
print(var_5)
var_5.reverse() # reverse the complete list
print(var_5)
var_5.sort() # sort the list in ascending order
print(var_5)
var_5.sort(reverse=True) # sort the list in descending 
print(var_5)

# boolean
var_7 = True

# dict - index, mutable, sequence, key:value pair
var_8 = {
    # 'key':value
    'name':"Hiran Ram Babu",
    'company': "Maho Jase IT",
    'mobile': 8825410600,
    'emailID': "info@mjit.in"
}

print(var_8.get('name')) # returns value for the specific key
print(var_8.items()) # returns dictionary
print(var_8.keys()) # returns only keys
print(var_8.values()) # returns only values
var_8['city'] = "Madurai" # to add a new key:value
print(var_8)
var_8['company'] = "MJIT" # replace a value for a specific key
print(var_8)
var_8.pop('city') # remove a specific key:value pair
print(var_8)