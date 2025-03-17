import random

print("Welcome to your pssword generator")

chars = """abcdefghijklmnopqrstuvqxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=";:'?.,}{][0123456789"""

number = int(input("How many password should we generate: "))

length = int(input("input passwrod length: "))

print('\n here are your passwords')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
    print("===================")