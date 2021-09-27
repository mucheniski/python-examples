# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'


def printLine():
    print()
    print('='*100)
    print()


def checkOption(playerOption):
    if playerOption == '1':
        return rock
    elif playerOption == '2':
        return paper
    elif playerOption == '3':
        return scissors


while True:

    player1Option = ''
    player2Option = ''

    # Two players choosing the option
    for i in range(1,3):
        printLine()
        print(f'Player {i}')
        print('1 - Rock | 2 - Paper | 3 - Scissors')
        option = str(input('Choose one option please: '))
        while option not in ('123'):
            option = str(input('Invalid option, please choose: '))
        if i == 1:
            player1Option = checkOption(option)
        elif i == 2:
            player2Option = checkOption(option)

    printLine()
    print(f'Player 1 option {player1Option}')
    print(f'Player 2 option {player2Option}')

    #  Rules of the game
    # Rock beats scissors
    if player1Option == rock and player2Option == scissors:
        print('Player 1 win!')
    # Scissors beats paper
    elif player1Option == scissors and player2Option == paper:
        print('Player 1 win!')
    # Paper beats rock
    elif player1Option == paper and player2Option == rock:
        print('Player 1 win!')
    else:
        print('Player 2 win!')

    printLine()
    # Choose if the players want to continue
    answer = str(input('Continue? Y ou N: ')).strip().upper()
    while answer not in 'YN':
        answer = str(input('Wrong value, do you want continue? Y ou N: ')).strip().upper()

    if answer == 'N':
        break
print('End of program')
