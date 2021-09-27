while True:
    print('Do something')

    answer = str(input('Continue? Y ou N: ')).strip().upper()
    while answer not in 'YN':
        answer = str(input('Wrong value, do you want continue? Y ou N: ')).strip().upper()

    if answer == 'N':
        break
print('End of program')