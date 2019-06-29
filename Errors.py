div = div42by
def div42by(divideBy):
    return 42 / divideBy

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))
#Printing out 42 / 0 won't allow it zerodivision error
#Try except statement:
div = div43by
def div43by(divideBy):
    try:
        return 43 / divideBy
    except ZeroDivisionError:
        print("Error - You tried to divide by zero!")

print(div43by(2))
print(div43by(12))
print(div43by(0))
print(div43by(1))


print("How many cats do you own?")
cats = input()
try:
    if int(cats) >= 4:
      print("That's a lot of cats!")
    else:
         print("That's not that many")
except ValueError:
     print("You didn't enter a number")


print("Recap:")
print("A divide-by-zero error happens when Python divides a number by zero")
print("Errors cause the program to crash")
print("An error that happens inside a try block will cause code in the except block to execute. That code can handle the error or display a message to the user so that the program can keep going.")
