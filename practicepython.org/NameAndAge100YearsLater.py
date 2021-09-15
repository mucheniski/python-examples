# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime

actualYear = datetime.date.today().year
name = str(input('Enter the name: '))
age = int(input('Enter the age: '))


# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
# (Hint: order of operations exists in Python)
timesToPrint = int(input('How many times do you want to print? '))


yearsTo100 = 100 - age
yearToComplete100 = actualYear + yearsTo100


# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
for i in range(0, timesToPrint):
    print(f'{name} has {age} years, and will complete 100 years old in {yearToComplete100}')

