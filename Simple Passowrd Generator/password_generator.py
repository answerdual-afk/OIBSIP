import string
import random

# Ask password length
pass_length = int(input('Enter the length of your password: '))

# Characters to use
characters = string.ascii_letters + string.digits

# Generate password
password = ''

for i in range(pass_length):
    password += random.choice(characters)

print('The password is:', password)