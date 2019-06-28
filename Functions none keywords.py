# This is about functions that you write on your own!
def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello World')

hello()
hello()
hello()

def name(name):
    print('Hello ' + name)

name('Alice')
name('Bob')
#Arguments allow us to pass values through to a variable inside the function, which is why name is in the perentheses,
#You can pass it any name and it will still work fine it doesn't have to be name. It's just a variable.

def plusOne(number):
    return number + 1
newNumber = plusOne(5)
print(newNumber)

#The none value is the lack of a value, it's the only function of its type.
None
spam = print()
print(spam)
#Keyword Arguments
print('Hello' end=' ')
print('World')
print('cat', 'dog', 'mouse' sep='&')

#Basic Recap:
print("Functions are like a mini-program inside your program.")
print("The main point of functions is to get rid of duplicate code.")
print("The def statement defines a function")
print("The input to functions are arguments. The output is the return value")
print("The parameters are the variables in between the function's parentheses in the def statement.")
print("The return value is specified using the return statement")
print("Every function has a return value. If your functions doesn't have a return statement, the default return value is None")
print("Keyword arguments to functions are usually for optional arguments.")
print("The print() function has keyword arguments end and sep")

