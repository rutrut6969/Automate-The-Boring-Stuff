#Recap on last video:
#Boolean Values are only True or False:
Rain = False
print("Is it rainging outside?")
Q = input()
if Q == 'yes':
      Rain = True
      print("Take an Umbrella with you!" + " Do you have one? ")
      Um = input()
      if Um == 'yes':
          print("Awesome go have fun!")
      elif Um == 'no':
          print("You'll get soaked if you don't!")
elif Q == 'no':
      print("Good go have a wonderful day!")
#This statement allows you to see how some booleans work!
"""
pet = 'Dog'
pet2 = 'Cat'
print(pet == 'Dog')     #True
print(pet == 'Cat')     #False
print(pet2 == 'Cat')    #True
print(pet2 == 'Dog')    #False
#Basically if the variable equals the statement then the statement is true
#Otherwise the statement will be false
print(42 == 42)
print(42 == 'Hello')
myAge = 22
print(myAge >= 22)
print(myAge < 30)
print(myAge > 30)
#I think you see the point!
"""
