

#multi_line = """I am a teacher and enjoy teaching.
#I didn't find anything as rewarding as empowering people.
#That is why I created 30 days of python"""
#print(multi_line)



# the %s is used for old style concatenation
first_name = "Asabaneh"
last_name = "Yetayeh"

#* %s becomes some sort of slot then its content will be in parenthesis with (%) operator 
#formatted_string = "I am %s %s . I teach %s" %(first_name,last_name,language)
#print(formatted_string)

#str.format() is a new style string formatting
#* In here the {} becomes a slot then its content is in the parenthesis with the .format() function
#formatted_string = "I am {} {}. I Teach {}".format(first_name,last_name,language)

#print(formatted_string)

#* string interpolation with f-strings

#print(f'I am {first_name} {last_name}. I Teach {language}')

#* Unpacking sequences of characters
language  = "Python"
a,b,c,d,e,f = language
l,e,t,t,e,r = language

"""
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
"""

#* Accessing characters by index
first_letter = language[0]
second_letter = language[1]
#print(first_letter)
#print(second_letter)

#* Accessing characters from right end
last_letter = language[-1]
second_last_letter = language[-2]
"""
print(last_letter)
print(second_last_letter)
"""
#* Slicing Python Strings
language = "Typescript"
#* Starts from index zero up to 3
first_three = language[0:4] # type
#print(first_three)
#* Another way
last_three = language[7:10]
#* print(last_three)
greeting = "Hello World"
# print(language[3:len(language)])

#* Reversing String
# print(greeting[::-1]) #dlroW olleH
# print(language[::-1])


#* Skipping characters while slicing
language = "Python"
greeting = "Hello World"
# First argument is start
# Second argument is stop
# Third argument is the step
#* Here we ar like saying that we are skipping two character at the time based on the third argument
pto = language[0:6:2]
# print(pto)
# print(greeting[0:len(greeting):3])


#* String methods

#* Capitalize first character of the letter
challenge  = "thirty days of python"
#print(challenge.capitalize())

#* Returns occurences of substring in string count
# count(substring,start,end)
# print(challenge.count("y")) # 3
# print(challenge.count("y",0,14)) #1

#* Checks if a string ends with a specified ending
challenge  = "thirty days of python"
# print(challenge.endswith('on')) # true
# print(challenge.endswith("tion")) # false

#* Replace tab with character spaces, default tab size is 8

challenge = "thirty\tdays\tof\tpython"
#overrides the default tab space of \t to 10 tabs spaces from the default 8
# print(challenge.expandtabs(10))

# *Returns the index of the first occurence of a substring, if none it returns -1
challenge = "thirty days of python"
# print(challenge.find('y')) # 5
# print(challenge.find('th')) # 0
# print(challenge.find("z")) # -1

#* Returns the index of the last occurence of a substring, if none returns -1
challenge = "thirty days of python"
# print(challenge.rfind('y')) # 16
# print(challenge.rfind('th')) # 17
# print(challenge.rfind("windyl")) # -1

#* Formatting a string
first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
job = 'teacher'
country = 'Finland'

# print(f'I am {first_name} my family name is {last_name} I am currently {age} years old my current job is {job} and currently residing in {country}')
print()

radius = 10
pi = 3.14
area = pi * radius ** 2
# print(f'The area of a circle with radius {radius} is {area}')



#* Returns the lowest index of a substring
#* has two optional arguments start and end which determines the starting and ending where to search from 
challenge = "thirty days of python"
sub_string = 'da'
# print(challenge.rindex(sub_string)) # 7
# print(challenge.rindex(sub_string,9))# error:substring not found

#* Checks string has  alphanumeric characters

challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # true

challenge = '30DaysPython'
print(challenge.isalnum()) # true

challenge = 'thirty days of python'
print(challenge.isalnum()) #False because of space , and space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) #false because of space






