def calculateValues(numberA, numberB, operation):
    """
    Check de operation informed from user
    :param operation:
    :return: operation
    """
    result = 0

    try:
        if operation == '+':
            result = numberA + numberB
        elif operation == '-':
            result = numberA - numberB
        elif operation == '/':
            result = numberA / numberB
        elif operation == '*':
            result = numberA * numberB
    except TypeError as error:
        print(f'Type error exception {error.__class__}')
    except ZeroDivisionError as error:
        print(f'Zero division error {error.__class__}')
    except Exception as error:
        print(f'Generic error exception {error.__class__}')
    else:
        print(f'The result is {result}')
    finally:
        print(f'End of transmission!')


try:
    numberA = int(input('Put the first value: '))
    numberB = int(input('Put the second value: '))

    operation = input('Choose the operation + - / *: ')
    while operation not in '+-/*':
        operation = input('Wrong answer, please choose the operation between + - / *: ')

    calculateValues(numberA, numberB, operation)
except ValueError as error:
    print(f'The informed value are wrong {error.__class__}')




