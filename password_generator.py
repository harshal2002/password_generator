import random

print('Password Generator is here to create passwords for you')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_.?'

number = input('How much passwords you want to generate?')
number = int(number)

length = input('Input your password length: ')
length = int(length)

print('\nYour passwords list is ready. Please check below:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)