import random

guess = int(input('Guess the number you rolled:\n'))


roll=random.randint(1, 6)

if guess == roll:
    print('You guessed correctly!')
else:
    print('You guessed wrong! The number was', roll)
    
