#python built in functions
#https://docs.python.org/3.9/library/functions.html

#*Common python functions

#checks count of the characters
print(len("hello2"))
#checks the data type
print(type("hello"))
#converts number to string
num = 10
con = str(num)
print(type(con))
#converts string to number
num = "10"
con = int(num)
print(type(con))
#converts integer to decimal
num = 10
con = float(num)
print(con)
#takes user input
"""
input = input("Enter your name:")
print(input)
"""


#help('keywords') -> shows a list of python reserved words
#help(str) -> giver information about string functions


print("Tested values: (20,30,40,50)");
#gives the minimum value
print("Minimum value : "+str(min(20,30,40,50)))
#gives maximum value
print("Maximum value : "+str(max(20,30,40,50)))
#takes an array and returns the min
print("Min from the list:"+str(min([20,30,40,50])))
#takes an array and returns the max
print("Max from the list:"+str(max([20,30,40,50])))
#takes only list as an argument and returns the sum of the values in the list
print("Sum of values in list:"+str(sum([20,30,40,50])));



#================================================================================
#*Variables
#mnemonic variable -> a variable name that can be easily remembered
#snake case -> recommended casing by pythond developers


first_name = "Windyl"
last_name = "Monton"
is_married = True
skilss = ["HTML","CSS","JS","React","Python"]
person_info = {
    'firstname' : "Windyl",
    "lastname" : "Monton",
    "country" : "Philippines",
}


#print can take unlimited paramaters
print("First Name Length:",len(first_name))
print("First Name:",first_name,"Last Name:",last_name)

#Declaring Mutiple Variable in a Line
#values assigned are the same order as how the variables are declared
first_name,last_name,country,age,is_married = "Windyl","Monton","Philippines",20,False

#Getting User Inout
first_name = input("What is your name:");
age = input("How old are you?:")

print("Name:",first_name)
print("Age:",age)

#==================================================================================
#*Data Types
#type() -> is used to identify a data type in python
print("Checking data types in python")
print(type("Windyl"))#str
print(type(first_name))#str
print(type(10))#int
print(type(3.14))#float
print(type(1 + 1j))#complex
print(type(True))#boolean
print(type([1,2,3,4]))#list
print(type({'name' : "Asabeneh"}))#dictionary
print(type((1,2)))#tuple
print(type(zip([1,2],[3,4])))#zip

#casting -> converting one data type to another datatype

#int to float
num_int = 10

print('num_int',num_int)
num_float = float(num_int)
print('num_float:',num_float)

#float to int
gravity = 9.81
print(int(gravity))

#int to str
num_str = str(10)

#str to int or float
print(int("10"))
print(float("10.6"))

#str to list
first_name = "Asabeneh"
print(first_name)
first_name_to_list = list(first_name)
print(first_name_to_list)



