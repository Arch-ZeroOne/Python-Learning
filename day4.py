

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
#print(last_three)
greeting = "Hello World"
#* Reversing String
print(greeting[::-1]) #dlroW olleH

#* Skipping characters while slicing

