import random

print("Random number generator")
print('Enter y to generate a new random number')
while input('generate [y/n]:') =='y':
    number = random.randint(1000,9999)
    print(f'lucky number: {number}')
print("Thanks for using")