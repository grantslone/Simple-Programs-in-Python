import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+`~[]{]\|;:,<.>/?'

welcomeMessage = "Welcome to the Password Generator!"
detailsMessage = "This program will generate a secure password using a random arrangement of letters (CAPS ON & caps off), numbers, and punctuations."
creatorMessage = "Created by Professor Renderer on October 3rd, 2018."



print(welcomeMessage + '\n' + detailsMessage + '\n' + creatorMessage + '\n')

passwordNum = input('How many passwords would you like to generate? ')
passwordNum = int(passwordNum)


passwordLength = input('How long will the password(s) be? ')
passwordLength = int(passwordLength)

print('\n')
print('Here are your password(s): \n')

for p in range(passwordNum):
    password = ''
    for c in range(passwordLength):
        password += random.choice(chars)
    print(password)

print('\n')
print('Thank you for using the Password Generator. Have a nice day!')

try:
    input("Press any key to continue...")
except SyntaxError:
    pass


