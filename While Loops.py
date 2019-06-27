
spam = 0
while spam < 5:  #While loop that ends with a condition
    print('Hello World')
    spam += 1



name = ''
while name != 'your name': #While loop
    print('Please type your name: ')
    name = input()
print('Thank You!')



while True:     # Infinit Loop
    print('Please type your name: ')
    name = input()
    if name == 'your name':
        break       #Breakpoints break out of the infinit loop
print('Thank You!')


spam = 0
while spam < 5:
    spam += 1
    print(spam)
    if spam == 3:
        continue    #Jumps loop back to top
    print('Hello World')


    
