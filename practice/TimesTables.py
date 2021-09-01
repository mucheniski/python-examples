def times(number, operation):
    """
    Print the times of a number
    :param number:
    :return: TimesTables from a number
    """
    print("=" * 100)
    print(f'Printing the times tables from {number}')
    print("=" * 100)
    print('')

    for i in range(1, 11):

        result = 0

        if operation == '+':
            result = number + i
        elif operation == '-':
            result = number - i
        elif operation == '*':
            result = number * i
        elif operation == '/':
            result = number / i

        print(f'{number} {operation} {i} = {result}')


number = int(input('Insert the number for a times tables: '))
operation = input('Choose the operation + - / *: ')
while operation not in '+-/*':
    operation = input('Wrong answer, please choose the operation between + - / *: ')

times(number, operation)
