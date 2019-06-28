#Variables can have the same name both in and out of a function. But are still considered two different variables
#spam = 42 #Global variable
eggs = 43

#Each function has a local scope.
#A scope is basically a container of variables, one variable cannot be both local and global scope.
def eggs2():
    spam = 42 #Local Variable

#A global scope is created when the program starts, and is destroyed when the program terminates.
#A local scope is created when a function is called and is destroyed when the function is over.
print("Code in the global scope cannot use any local variables.")
print("Code in a local scope can access global variables.")
print("Code in one function's local scope cannot use variables in another local scope.")
print("Code in one funcion's local scope cannot user variable in any other local scope.")
def bacon():
    ham = 101
    eggs = 0
    print("Eggs for bacon = " + (str(eggs)) + " Ham = " + str(ham) + "!")

def spam():
    eggs = 99
    bacon()
    print(eggs) #Will print out 99 because bacon's local scope has been destroyed by the time it prints the eggs variable so it'll print instead for spam


spam()
print(eggs)
#This causes an error because it's outside the local scope of the variable.

def ham():
    print(eggs)


spam()

#Global statement:
def blah():
    global eggs
    eggs = 99
    print(eggs)

print("Recap:")
print("A scope can be thought of as an aarea of the source code, and as a  container of variables.")
print("The global scope is code outside of all functions. Variables assigned here are global variables.")
print("Each function's code is in its own local scope. Variables assigned here are local variables.")
print("Code in the global scope cannot use any local variables.")
print("Code ina function's local scope cannot use variables in any other function's local scope.")
print("If there's an assignment statement for a variable in a function, that is a local variable.")
