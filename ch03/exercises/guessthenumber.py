import random

num1 = random.randint(1,10)
guess = input

print('guess a number between one and ten.')
guess = input()
guess = int(guess)
    
if guess > num1:
    print('too big')

if guess < num1:
    print('too small')

if guess == num1:
    print('correct')

