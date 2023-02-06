# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

# print(myint)
# print(myfloat)
# print(mystr)
# print(mybool)
# print(mylist)
# print(mytuple)
# print(mydict, "\n")

# re-declaring a variable
mybool = False
print(mybool) 
# accessing a member of a sequence type
print(mylist[2]) 
# using slices to get parts of a sequence
print(mylist[1:5])
print(mylist[1:5:2])
# using slices to reverse a sequence
print(mylist[::-1])
# dictionaries are accessed via keys
print(mydict["two"])
# ERROR: variables of different types cannot be combined
#print("string" + 123)
print("string" + str(123))
# Global vs. local variables in functions
def somefunction():
    global mystr # Use this to affect the global variable outside this function
    mystr = "def"
    print(mystr)

somefunction()
print(mystr)
del mystr # Deletes a variable's definition
print(mystr) # Cannot print, since the variable has been undefined.