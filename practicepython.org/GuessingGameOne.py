# https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
import random

answer = ''

while True:

    randomNumber = random.randint(1, 9)
    print(f'Computer number {randomNumber}')

    chosenNumber = int(input('Please choose one number between 1 and 9: '))

    if chosenNumber < randomNumber:
        print('To low')
    elif chosenNumber > randomNumber:
        print('to righ')
    else:
        print('You win!')

    answer = str(input('To stop type exit to continue press ENTER ')).strip().upper()
    if answer == 'EXIT':
        break
print('End of game')


