# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

def printLine():
    print()
    print('='*100)
    print()


# text = str(input('type a phrase'))
# phrase = text.strip().upper()
phrase = 'APOS A SOPA'.strip().upper()

print(f'Typed text{phrase}')
printLine()

words = phrase.split()
print(f'words {words}')
printLine()

together = ''.join(words)
print(f'words together without spaces {together}')
printLine()

invert = together[::-1]
print(f'inverted {invert}')
printLine()

if invert == together:
    print('Palindrome')
else:
    print('Not palindrome')

