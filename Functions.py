#Python comes with a bunch of built in functions:
print("The print function allows you to print to the command screen in the terminal to recieve information")
print(len('This will print out the length of this string, all characters are included'))
#You need to use the print function to get any information including when you're trying to get the length of a string or set of strings
var = 'this is a variable'
#To receive information from this variable you need to print it out:
print(var)
print(len(var))
#The first will just print what is inside of the variable var
#The second will prit how many characters are inside the variable
name = ''
print("What's your name?:")
name = input(':> ')
print("Hello " + name + "!")
#This will ask for an input from the user, and then print hello and the users name they specified.
#Python comes with a standard library with a group of modules
#You need to import the module using an import statement
import random
print(random.randint(1, 10))
#Since randint is inside the random module you have to use 'random.'
#In order to be able to utilize it
from random import *
print(randint(1, 10))
#It is better to use the regular version of importing this for code reading purposes
#There are third party modules you can download and utilize as well! It's not hard as long as you know the pip tool
import pyperclip
pyperclip.copy("HelloWorld")
pyperclip.paste()
#This allows you to copy text to the clipboard and paste it out.
#pyperclip is a third party module


#This is a workaround to the 'random.' thing EX:
randint(1,10)
#Using the nomal form is better for reading code
import sys
#This will exit the program essentially
print("Hello")
sys.exit()
print("Goodbye")


