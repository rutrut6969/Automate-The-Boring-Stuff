#Guess the number game!
import random
print("Hello what is your name?")
name = input(":> ")

print("Well " + name + " I'm thinking of a number between 1 and 20")
secretNumber = random.randint(1, 20)

for guessestaken in range(1, 7):
    print("Take a guess")
    guess = int(input(":> "))

    if guess < secretNumber:
        print("That's to low! Try going a little higher")
    elif guess > secretNumber:
        print("That one is too high!")
    else:
        break #This condition is for the correct guess!
if guess == secretNumber:
    print("Awesome work " + name + "! You guessed correctly in " + str(guessestaken) + " guesses!")
else:
    print("Not quite, The guess I was thinking of was " + str(secretNumber))


